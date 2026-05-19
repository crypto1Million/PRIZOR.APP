from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import secrets

from backend.database import get_db
from backend import models
from backend.core.security import hash_password
from backend.core.email import send_reset_email

router = APIRouter()


@router.post("/forgot-password")
def forgot_password(email: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    token = secrets.token_urlsafe(32)

    user.reset_token = token
    user.reset_token_expiry = datetime.utcnow() + timedelta(hours=1)

    db.commit()

    reset_link = f"http://localhost:3000/reset-password/{token}"

    send_reset_email(user.email, reset_link)

    return {
        "message": "Reset email sent"
    }


@router.post("/reset-password")
def reset_password(
    token: str,
    new_password: str,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.reset_token == token
    ).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")

    if user.reset_token_expiry < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Token expired")

    user.hashed_password = hash_password(new_password)

    user.reset_token = None
    user.reset_token_expiry = None

    db.commit()

    return {
        "message": "Password updated"
    }