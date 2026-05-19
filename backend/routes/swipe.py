from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.routes.auth import get_current_user
import models, schemas
from datetime import datetime, timedelta 
from backend.core.notifications import send_push_notification
from backend.core.discovery import calculate_discover_score
from backend.models.match import Match
from backend.core.analytics import track_event
import random
from sqlalchemy import func

router = APIRouter(prefix="/swipe", tags=["Swipe"])

# ==============================
# DB Dependency
# ==============================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================
# 🧠 ELO FUNCTION
# ==============================
def update_elo(viewer, target, liked, k=16):
    expected_viewer = 1 / (1 + 10 ** ((target.elo_score - viewer.elo_score) / 400))
    expected_target = 1 - expected_viewer

    if liked:
        viewer_score = 1
        target_score = 1
    else:
        viewer_score = 0.3
        target_score = 0.7

    viewer.elo_score += int(k * (viewer_score - expected_viewer))
    target.elo_score += int(k * (target_score - expected_target))


# ==============================
# 🔥 SWIPE ROUTE
# ==============================
@router.post("/")
def swipe(
    swipe_data: schemas.SwipeCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    now = datetime.utcnow()

    # ==============================
    # 👤 GET CURRENT USER
    # ==============================
    current = db.query(models.User).filter(
        models.User.id == current_user
    ).first()

    if not current:
        return {"error": "User not found"}

    # ==============================
    # 🚫 ANTI-SPAM PROTECTION
    # ==============================

    # Reset daily counter
    if not current.last_swipe_reset or (now - current.last_swipe_reset).days >= 1:
        current.swipes_today = 0
        current.last_swipe_reset = now

    # Daily limit
    if current.swipes_today >= 200:
        return {"error": "Daily swipe limit reached"}

    # Cooldown
    if current.last_swipe_time:
        diff = (now - current.last_swipe_time).seconds
        if diff < 2:
            return {"error": "You're swiping too fast"}

    # Update tracking
    current.last_swipe_time = now
    current.swipes_today += 1

    # ==============================
    # 🎯 GET TARGET USER
    # ==============================
    target_user = db.query(models.User).filter(
        models.User.id == swipe_data.swiped_user_id
    ).first()

    if not target_user:
        return {"error": "Target user not found"}

    # ==============================
    # 💾 SAVE SWIPE
    # ==============================
    new_swipe = models.Swipe(
        user_id=current_user,
        swiped_user_id=swipe_data.swiped_user_id,
        liked=swipe_data.liked
    )
    db.add(new_swipe)

    # CHECK IF OTHER USER ALREADY LIKED CURRENT USER

    existing_like = db.query(models.Swipe).filter(
       models.Swipe.swiper_id == swiped_id,
       models.Swipe.swiped_id == current_user.id,
       models.Swipe.is_like == True
    ).first()


    # CREATE MATCH

    if existing_like and is_like:

        match = models.Match(
        user1_id=current_user.id,
        user2_id=swiped_id
    )

    db.add(match)
    db.commit()
    
    track_event(
        db,
        current_user.id,
        "match_created"
    )

    track_event(
        db,
        swiped_id,
        "match_created"
    )

    if is_like:

       track_event(
           db,
           current_user.id,
           "swipe_like"
        )

    else:

        track_event(
            db,
            current_user.id,
            "swipe_pass"
        )

    return {
        "match": True
    }

    # ==============================
    # ❤️ LIKE LOGIC
    # ==============================
    if swipe_data.liked:
        target_user.likes_received += 1

    # ==============================
    # ⚡ ACTIVITY TRACKING
    # ==============================
    current.swipes_done += 1
    current.last_active = now

    # ==============================
    # 🧠 ELO UPDATE
    # ==============================
    update_elo(current, target_user, swipe_data.liked)

    from core.discovery import calculate_discover_score

    current.core.discover_score = calculate_discover_score(current)
    target_user.core.discover_score = calculate_discover_score(target_user)

    # ==============================
    # 💖 MATCH CHECK
    # ==============================
    match = db.query(models.Swipe).filter(
        models.Swipe.user_id == swipe_data.swiped_user_id,
        models.Swipe.swiped_user_id == current_user,
        models.Swipe.liked == True
    ).first()

    is_match = False

    if swipe_data.liked and match:

        if target_user.fcm_token:

        send_push_notification(
           target_user.fcm_token,
           "New Match ❤️",
           f"You matched with {current.username}"
       )

        is_match = True

        # 🔥 ELO BONUS
        current.elo_score += 25
        target_user.elo_score += 25

        # 🚀 MATCH BOOST
        current.boost_active = True
        current.boost_multiplier = 2
        current.boost_expires_at = now + timedelta(minutes=15)

        target_user.boost_active = True
        target_user.boost_multiplier = 2
        target_user.boost_expires_at = now + timedelta(minutes=15)

    # ==============================
    # 🚀 HIGH ELO BOOST
    # ==============================
    if current.elo_score > 1200:
        current.boost_active = True
        current.boost_multiplier = 2
        current.boost_expires_at = now + timedelta(minutes=30)

    # ==============================
    # 📊 BEHAVIOR TRACKING
    # ==============================
    behavior = db.query(models.UserBehavior).filter(
        models.UserBehavior.user_id == current_user,
        models.UserBehavior.target_user_id == swipe_data.swiped_user_id
    ).first()

    if not behavior:
        behavior = models.UserBehavior(
            user_id=current_user,
            target_user_id=swipe_data.swiped_user_id
        )
        db.add(behavior)

    if swipe_data.liked:
        behavior.likes += 1
    else:
        behavior.dislikes += 1

    # ==============================
    # 💾 FINAL COMMIT
    # ==============================
    db.commit()

    return {
        "message": "Swipe recorded",
        "match": is_match
    }

# ==============================
# BOOST ACTIVATION 
# ==============================
@router.post("/boost")
def activate_boost(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    user = db.query(models.User).filter(
        models.User.id == current_user
    ).first()

    if not user:
        return {"error": "User not found"}

    # Activate boost (example: 1 hour)
    user.boost_active = True
    user.boost_multiplier = 3
    user.boost_expires_at = datetime.utcnow() + timedelta(hours=1)

    db.commit()

    return {"message": "Boost activated 🚀"}


# ==============================
# ELO UPDATE FUNCTION (OPTIMIZED)
# ==============================
def update_elo(viewer, target, liked, k=16):
    expected = 1 / (1 + 10 ** ((target.elo_score - viewer.elo_score) / 400))

    if liked:
        score = 1
    else:
        score = 0.3  

    change = int(k * (score - expected))

    target.elo_score += change


# ==============================
# 🧠 SCORING FUNCTION
# ==============================
def score(u, current_user_id, db):
    like_ratio = u.likes_received / (u.swipes_done + 1)

    # Activity boost
    if u.last_active:
        seconds = (datetime.utcnow() - u.last_active).seconds
        activity_score = 1 / (seconds + 1)
    else:
        activity_score = 0

    # Avoid repeat profiles
    swiped_before = db.query(models.Swipe).filter(
        models.Swipe.user_id == current_user_id,
        models.Swipe.swiped_user_id == u.id
    ).first()

    exposure_penalty = 0.5 if swiped_before else 1

    # Boost if they liked you
    liked_you = db.query(models.Swipe).filter(
        models.Swipe.user_id == u.id,
        models.Swipe.swiped_user_id == current_user_id,
        models.Swipe.liked == True
    ).first()

    match_boost = 2 if liked_you else 1

    return (
        (like_ratio * 0.4) +
        (activity_score * 0.3)
    ) * exposure_penalty * match_boost


# ==============================
# 🚀 SMART FEED
# ==============================
@router.get("/feed")
def smart_feed(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    user = db.query(models.User).filter(models.User.id == current_user).first()

    if not user:
        return {"error": "User not found"}

    # ==============================
    # 🔥 FETCH USERS
    # ==============================
    users = db.query(models.User).filter(
        models.User.gender == user.preference,
        models.User.id != user.id
    ).all()

    user_ids = [u.id for u in users]

    # ==============================
    # 🔥 ADD THIS BLOCK HERE 👇
    # ==============================

    behavior_data = db.query(models.UserBehavior).filter(
        models.UserBehavior.user_id == current_user
    ).all()

    behavior_map = {
        b.target_user_id: b
        for b in behavior_data
    }

    # ==============================
    # 🔥 BULK FETCH SWIPE DATA
    # ==============================

    # Users you already swiped
    swiped_map = {
        s.swiped_user_id: True
        for s in db.query(models.Swipe)
        .filter(models.Swipe.user_id == current_user)
        .all()
    }

    # Users who liked YOU
    liked_you_map = {
        s.user_id: True
        for s in db.query(models.Swipe)
        .filter(
            models.Swipe.swiped_user_id == current_user,
            models.Swipe.liked == True
        ).all()
    }

    # ==============================
    # 🧠 SCORING FUNCTION (OPTIMIZED)
    # ==============================
    def score(u):
        like_ratio = u.likes_received / (u.swipes_done + 1)

        # Activity
        if u.last_active:
            seconds = (datetime.utcnow() - u.last_active).seconds
            activity_score = 1 / (seconds + 1)
        else:
            activity_score = 0

        exposure_penalty = 0.5 if u.id in swiped_map else 1
        match_boost = 2 if u.id in liked_you_map else 1

        # 👇 NEW: ELO factor (we’ll define next)
        elo_score = u.elo_score if hasattr(u, "elo_score") else 1000

        # BOOST LOGIC
        boost = 1

        if u.boost_active and u.boost_expires_at:
            if u.boost_expires_at > datetime.utcnow():
               boost = u.boost_multiplier
            else:
                u.boost_active = False  # auto-expire
                boost = 1

        # 🔥 PERSONAL BEHAVIOR SCORE
        behavior = db.query(models.UserBehavior).filter(
           models.UserBehavior.user_id == current_user,
        models.UserBehavior.target_user_id == u.id
        ).first()

        if behavior:
            behavior_score = (behavior.likes + 1) / (behavior.dislikes + 1)
        else:
            behavior_score = 1

        return (
          (like_ratio * 0.3) +
          (activity_score * 0.2) +
          (elo_score / 1000 * 0.5)
        ) * exposure_penalty * match_boost * boost

    ranked_users = sorted(
        candidate_users,
        key=lambda x: calculate_discovery_score(x),
        reverse=True
    )

    return ranked_users[:20]