from sqlalchemy.orm import Session

from backend.models.user import User
from backend.models.follow import Follow


class CreatorDashboardService:

    @staticmethod
    def get_dashboard(
        db: Session,
        creator_id: int
    ):

        creator = (
            db.query(User)
            .filter(User.id == creator_id)
            .first()
        )

        if not creator:
            return None

        followers = (
            db.query(Follow)
            .filter(
                Follow.following_id == creator_id
            )
            .count()
        )

        return {
            "creator_id": creator.id,
            "username": creator.username,

            "creator_level": getattr(
                creator,
                "creator_level",
                1
            ),

            "followers": followers,

            "revenue_usd": getattr(
                creator,
                "revenue_usd",
                0
            ),

            "crypto_revenue": getattr(
                creator,
                "crypto_revenue",
                0
            ),

            "rank": getattr(
                creator,
                "creator_rank",
                None
            ),

            "verification": getattr(
                creator,
                "creator_verified",
                False
            )
        }