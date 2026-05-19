from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from datetime import datetime
from core.security import hash_password
from routes.auth import get_current_user
from core.recommendation import calculate_recommendation_score
from core.trust import calculate_trust
import models
import schemas   # ✅ IMPORTANT

router = APIRouter(prefix="/users", tags=["Users"])

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
# CURRENT USER (PROTECTED)
# ==============================
@router.get("/me")
def get_me(user = Depends(get_current_user)):
    return {"user_id": user}

# ==============================
# REGISTER USER
# ==============================
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_pw = hash_password(user.password)

    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_pw
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.get("/discover")
def discover_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    current = db.query(models.User).filter(
        models.User.id == current_user
    ).first()

    # Already swiped users
    swiped_ids = db.query(
        models.Swipe.swiped_user_id
    ).filter(
        models.Swipe.user_id == current_user
    ).all()

    swiped_ids = [u[0] for u in swiped_ids]

    blocked_ids = db.query(
        models.Block.blocked_user_id
    ).filter(
        models.Block.blocker_id == current_user
    ).all()

    blocked_ids = [b[0] for b in blocked_ids]

    # Candidate users
    users = db.query(models.User).filter(

        models.User.id != current_user,

        ~models.User.id.in_(swiped_ids),

        models.User.profile_image != None,

        models.User.activity_score > 5,

        models.User.age >= current.preferred_age_min,

        models.User.age <= current.preferred_age_max

        ~models.User.id.in_(blocked_ids),

    ).all()

    ranked = []

    for user in users:

        score = calculate_recommendation_score(
            current,
            user
        )

        ranked.append({
            "user": user,
            "score": score
        })

    # Highest recommendation first
    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked[:50]


# ==============================
# GET USERS
# ==============================
@router.get("/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.put("/profile")
def update_profile(
    data: schemas.ProfileUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user = db.query(models.User).filter(
        models.User.id == current_user
    ).first()

    user.bio = data.bio
    user.age = data.age
    user.interests = data.interests
    user.trust_score = calculate_trust(user)

    # ==============================
    # PROFILE COMPLETION
    # ==============================
    completion = 0

    if user.bio:
        completion += 25

    if user.profile_image:
        completion += 25

    if user.age:
        completion += 25

    if user.interests:
        completion += 25

    user.profile_completion = completion

    db.commit()

    return {
        "message": "Profile updated"
    }

# ==============================
# GET FILTERED USERS
# ==============================
@router.get("/feed")
def smart_feed(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return {"status": "feed working"} 
    
    user = db.query(models.User).filter(models.User.id == current_user).first()

    users = db.query(models.User).filter(
        models.User.gender == user.preference,
        models.User.id != user.id
    ).all()

    # 🔥 ADD THIS FUNCTION HERE
    def score(u):
        like_ratio = (u.likes_received / (u.swipes_done + 1))

        if u.last_active:
            time_diff = (datetime.utcnow() - u.last_active).total_seconds()
            activity_score = 1 / (time_diff + 1)
        else:
            activity_score = 0

        return (like_ratio * 0.6) + (activity_score * 0.4)

    # 🔥 SORT USERS
    ranked = sorted(users, key=score, reverse=True)

    return ranked   

@router.post("/fcm-token")
def save_fcm_token(
    token: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user = db.query(models.User).filter(
        models.User.id == current_user
    ).first()

    if not user:
        return {"error": "User not found"}

    user.fcm_token = token

    db.commit()

    return {
        "message": "FCM token saved"
    }    