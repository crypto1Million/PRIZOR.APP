from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.services.profile_service import ProfileService

router = APIRouter(
    prefix="/profile",
    tags=["Achievements"]
)


@router.get("/{user_id}/achievements")
def achievements(
    user_id: int,
    db: Session = Depends(get_db)
):
    return ProfileService.get_profile_achievements(
        db,
        user_id
    )