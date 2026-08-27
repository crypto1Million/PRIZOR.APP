from sqlalchemy.orm import Session

from backend.models.user import User
from backend.models.follow import Follow
from backend.models.achievement import Achievement
from backend.models.user_achievement import UserAchievement


class ProfileService:

    @staticmethod
    def get_profile(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None

        followers = (
            db.query(Follow)
            .filter(Follow.following_id == user_id)
            .count()
        )

        following = (
            db.query(Follow)
            .filter(Follow.follower_id == user_id)
            .count()
        )

        achievements = (
            db.query(UserAchievement)
            .filter(UserAchievement.user_id == user_id)
            .count()
        )

        return {
            "id": user.id,
            "username": user.username,
            "email": getattr(user, "email", None),

            "followers": followers,
            "following": following,
            "achievements": achievements,

            "verified": getattr(user, "verified", False),
            "creator_verified": getattr(
                user,
                "creator_verified",
                False
            )
        }

    @staticmethod
    def get_profile_achievements(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Achievement)
            .join(
                UserAchievement,
                Achievement.id ==
                UserAchievement.achievement_id
            )
            .filter(
                UserAchievement.user_id == user_id
            )
            .all()
        )