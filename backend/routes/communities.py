from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.community import Community
from backend.models.community_member import CommunityMember

router = APIRouter(
    prefix="/profile",
    tags=["Communities"]
)


@router.get("/{user_id}/communities")
def user_communities(
    user_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Community)
        .join(
            CommunityMember,
            Community.id ==
            CommunityMember.community_id
        )
        .filter(
            CommunityMember.user_id ==
            user_id
        )
        .all()
    )