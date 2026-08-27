from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.services.followers_service import FollowersService

router = APIRouter(
    prefix="/profile",
    tags=["Followers"]
)


@router.get("/{user_id}/followers")
def get_followers(
    user_id: int,
    db: Session = Depends(get_db)
):
    return FollowersService.get_followers(
        db,
        user_id
    )


@router.get("/{user_id}/following")
def get_following(
    user_id: int,
    db: Session = Depends(get_db)
):
    return FollowersService.get_following(
        db,
        user_id
    )