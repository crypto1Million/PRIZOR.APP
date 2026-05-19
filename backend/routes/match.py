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