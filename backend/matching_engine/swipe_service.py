from sqlalchemy.orm import Session

from backend.models.swipe import Swipe


class SwipeService:

    @staticmethod
    def swipe(
        db: Session,
        user_id: int,
        target_id: int,
        action: str,
    ):

        allowed = {
            "like",
            "pass",
            "super_like",
        }

        if action not in allowed:
            raise ValueError(
                "Invalid swipe action"
            )

        swipe = Swipe(
            user_id=user_id,
            target_user_id=target_id,
            action=action,
        )

        db.add(swipe)
        db.commit()
        db.refresh(swipe)

        return swipe