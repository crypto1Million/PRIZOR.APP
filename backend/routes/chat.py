from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func 
from backend.database import SessionLocal
from schemas import MessageCreate
from routes.auth import get_current_user
from fastapi import APIRouter, WebSocket, WebSocketDisconnect 
from utils.socket_manager import manager
from fastapi import HTTPException
from datetime import datetime  
from core.notifications import send_push_notification
from core.moderation import contains_banned_content
from backend.core.redis import redis_client
from backend.core.analytics import track_event
import models
import datetime 

router = APIRouter(prefix="/chat", tags=["Chat"])

# ✅ DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ SEND MESSAGE
@router.post("/send/{receiver_id}")
def send_message(
    msg: MessageCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # 🔒 CHECK MATCH FIRST
    match = db.query(models.Match).filter(
        ((models.Match.user1_id == current_user) & (models.Match.user2_id == receiver_id)) |
        ((models.Match.user1_id == receiver_id) & (models.Match.user2_id == current_user))
    ).first()

    if not match:
        raise HTTPException(status_code=403, detail="You can only message matched users")

    # ✅ SEND MESSAGE
    message = models.Message(
        sender_id=current_user,
        receiver_id=receiver_id,
        content=msg.content
    )

    db.add(message)
    db.commit()

    return {"status": "sent"}

# ✅ GET MESSAGES
@router.get("/messages/{user1}/{user2}")
def get_messages(user1: str, user2: str, db: Session = Depends(get_db)):
    return db.query(models.Message).filter(
        ((models.Message.sender_id == user1) & (models.Message.receiver_id == user2)) |
        ((models.Message.sender_id == user2) & (models.Message.receiver_id == user1))
    ).all()

# WEBSOCKET FOR REAL-TIME CHAT
@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)

    redis_client.set(
        f"user:{user_id}:online",
        "1",
        ex=300
    )

    redis_client.set(
        f"typing:{chat_id}:{user_id}",
        "1",
        ex=5
    ) 

    redis_client.set(
        f"seen:{message_id}",
        "1",
        ex=86400
    )

    user = db.query(models.User).filter(
       models.User.id == user_id
    ).first()

    if user:
        user.is_online = True
        db.commit()

    db = SessionLocal()

    try:
        while True:
            data = await websocket.receive_json()

            # ==============================
            # 📩 MESSAGE
            # ==============================
            if data.get("type") == "message":

                receiver_id = data["receiver_id"]
                message = data["message"]

            is_blocked = db.query(models.Block).filter(
                (
                    (models.Block.blocker_id == user_id) &
                    (models.Block.blocked_id == receiver_id)
                ) |
                (
                    (models.Block.blocker_id == receiver_id) &
                    (models.Block.blocked_id == user_id)
                )
            ).first()

            if is_blocked:

                await websocket.send_json({
                   "error": "User unavailable"
                })

                return


            elif data.get("type") == "seen":

                message_id = data["message_id"]

                msg = db.query(models.Message).filter(
                    models.Message.id == message_id
                ).first()

                if msg and msg.receiver_id == user_id:

                   msg.is_seen = True
                   msg.seen_at = datetime.utcnow()

                   db.commit()

                   await manager.send_personal(msg.sender_id, {
                       "type": "seen",
                       "message_id": msg.id
                    })

               
            elif data.get("type") == "typing":

                receiver_id = data["receiver_id"]

                if manager.is_connected(receiver_id):

                    await manager.send_personal(receiver_id, {
                        "type": "typing",
                        "from": user_id
                    })    
            
            elif data.get("type") == "stop_typing":

                receiver_id = data["receiver_id"]

                if manager.is_connected(receiver_id):

                    await manager.send_personal(receiver_id, {
                        "type": "stop_typing",
                        "from": user_id
                })


            # ==============================
            # 🚫 CONTENT MODERATION
            # ==============================
            if contains_banned_content(message):

                await websocket.send_json({
                    "error": "Message blocked"
                })

                continue

                is_match = db.query(models.Match).filter(
                    (
                        (models.Match.user1_id == user_id) &
                        (models.Match.user2_id == receiver_id)
                    ) |
                    (
                        (models.Match.user1_id == receiver_id) &
                        (models.Match.user2_id == user_id)
                    )
                ).first()


                if not is_match:

                    await websocket.send_json({
                    "error": "You can only message matched users"
                    })      

                    continue

            # (KEEP your match validation here if you have it)

                new_msg = models.Message(
                    sender_id=user_id,
                    receiver_id=receiver_id,
                    content=message
                )

                db.add(new_msg)

                conv = get_conversation(db, user_id, receiver_id)

                if not conv:
                    conv = models.Conversation(
                       user1_id=user_id,
                       user2_id=receiver_id,
                       last_message=message,
                       last_message_time=datetime.utcnow(),
                       unread_user1=0,
                       unread_user2=1
                    )
                    db.add(conv)

                else:
                    conv.last_message = message
                    conv.last_message_time = datetime.utcnow()

                    if user_id == conv.user1_id:
                        conv.unread_user2 += 1
                    else:
                        conv.unread_user1 += 1

                db.commit()

                track_event(
                    db,
                    user_id,
                    "message_sent"
                )
            
                
                # ==============================
                # 👤 GET RECEIVER
                # ==============================
                receiver = db.query(models.User).filter(
                   models.User.id == receiver_id
                ).first()

                # ==============================
                # 🔔 PUSH NOTIFICATION
                # ==============================
                if receiver and receiver.fcm_token:

                    send_push_notification(
                        receiver.fcm_token,
                        "New Message 💬",
                        message
                    )
        
                if manager.is_connected(receiver_id):
                    db.query(models.Message).filter(
                       models.Message.id == new_msg.id
                    ).update({
                       "is_delivered": True,
                       "delivered_at": datetime.utcnow()
                    })
                    db.commit()

                    await manager.send_personal(receiver_id, {
                        "type": "message",
                        "from": user_id,
                        "message": message
                    })

                    await manager.send_personal(user_id, {
                        "type": "delivered",
                        "message_id": new_msg.id
                    })

            # ==============================
            # ⚡ TYPING
            # ==============================
            elif data.get("type") == "typing":
              receiver_id = data["receiver_id"]
              await manager.send_personal(receiver_id, {
                  "type": "typing",
                  "from": user_id
                })

            # ==============================
            # ✅ READ RECEIPTS
            # ==============================
            elif data.get("type") == "read":
                sender_id = data["sender_id"]
           
                # 🔒 PROTECTION GOES HERE
                if sender_id == user_id:
                    continue

                db.query(models.Message).filter(
                    models.Message.sender_id == sender_id,
                    models.Message.receiver_id == user_id,
                    models.Message.is_read == False
                ).update({
                    "is_read": True,
                    "read_at": datetime.utcnow()
                })

                db.commit()

                # reset unread count in conversation
                conv = get_conversation(db, user_id, sender_id)

                if conv:
                    if user_id == conv.user1_id:
                      conv.unread_user1 = 0
                    else:
                      conv.unread_user2 = 0

                    db.commit()

                await manager.send_personal(sender_id, {
                    "type": "read_receipt",
                    "by": user_id
               })

            receiver_id = data["receiver_id"]
            message = data["message"]


            # ==============================
            # 🔒 MATCH VALIDATION (IMPORTANT)
            # ==============================
            match = db.query(models.Swipe).filter(
                models.Swipe.user_id == receiver_id,
                models.Swipe.swiped_user_id == user_id,
                models.Swipe.liked == True
            ).first()

            if not match:
                await websocket.send_json({"error": "Not matched"})
                continue

            # ==============================
            # 💾 SAVE MESSAGE
            # ==============================
            new_msg = models.Message(
                sender_id=user_id,
                receiver_id=receiver_id,
                content=message
            )

            db.add(new_msg)
            db.commit()

            # ==============================
            # 🚀 SEND REALTIME
            # ==============================

            payload = {
                "from": user_id,
                "message": message
            }

            # Send to receiver instantly
            await manager.send_personal(receiver_id, payload)
            

    except WebSocketDisconnect:

        redis_client.delete(f"user:{user_id}:online")
        redis_client.sadd("online_users", user_id)
        redis_client.srem("online_users", user_id)

        user = db.query(models.User).filter(
            models.User.id == user_id
        ).first()

        if user:
            user.is_online = False
            user.last_seen = datetime.utcnow()

            db.commit()

        manager.disconnect(user_id, websocket)

    finally:
        db.close()

@router.get("/list")
def chat_list(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    convs = db.query(models.Conversation).filter(
        (models.Conversation.user1_id == current_user) |
        (models.Conversation.user2_id == current_user)
    ).order_by(models.Conversation.last_message_time.desc()).all()

    chats = []

    for c in convs:
        # Identify the other user
        other_user = c.user2_id if c.user1_id == current_user else c.user1_id

        # Get unread count directly (NO QUERY)
        unread = c.unread_user1 if current_user == c.user1_id else c.unread_user2

        chats.append({
            "user_id": other_user,
            "last_message": c.last_message,
            "timestamp": c.last_message_time,
            "unread": unread
        })

    return chats        

def get_conversation(db, user1, user2):
    return db.query(models.Conversation).filter(
        ((models.Conversation.user1_id == user1) & (models.Conversation.user2_id == user2)) |
        ((models.Conversation.user1_id == user2) & (models.Conversation.user2_id == user1))
    ).first()    