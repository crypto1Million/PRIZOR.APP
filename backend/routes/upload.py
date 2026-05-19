from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import cloudinary.uploader

from backend.database import get_db
from routes.auth import get_current_user
from core.cloudinary_config import *
from core.image_moderation import check_image_safe
from core.trust import calculate_trust
from backend.core.image_pipeline import process_profile_image
import models

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("/")
async def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    # ==============================
    # ☁️ UPLOAD TO CLOUDINARY
    # ==============================
    image_url = process_profile_image(file.file)

    user.profile_image = result["secure_url"]

    user.trust_score = calculate_trust(user)

    safe = check_image_safe(user.profile_image)

    if not safe:
        return {"error": "NSFW image detected"}

    image_url = result["secure_url"]

    # ==============================
    # 👤 GET USER
    # ==============================
    user = db.query(models.User).filter(
        models.User.id == current_user
    ).first()

    if not user:
        return {"error": "User not found"}

    # ==============================
    # 🖼 SAVE IMAGE URL
    # ==============================
    user.profile_image = image_url

    db.commit()

    return {
        "message": "Image uploaded",
        "image_url": image_url
    }