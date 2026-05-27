from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from routes.auth import get_current_user
import models

router = APIRouter(prefix="/match", tags=["Match"])

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
# GET MATCHES
# ==============================
@router.get("/")
def get_matches(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    matches = db.query(models.Match).filter(
        (models.Match.user1_id == user_id) |
        (models.Match.user2_id == user_id)
    ).all()

    return matches

@router.get("/matches/{match_user_id}/insights")

def get_match_insights(
    match_user_id: int,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    match_user = db.query(models.User).filter(
        models.User.id == match_user_id
    ).first()

    if not match_user:
        return {"error": "User not found"}

    insights = generate_match_insight(
        current_user,
        match_user
    )

    score = calculate_compatibility_score(
        current_user,
        match_user
    )

    return {
        "compatibility_score": score,
        "insights": insights
    }


