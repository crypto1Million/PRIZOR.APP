from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.services.profile_service import ProfileService

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/{user_id}")
def get_profile(
    user_id: int,
    db: Session = Depends(get_db)
):
    profile = ProfileService.get_profile(
        db,
        user_id
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile