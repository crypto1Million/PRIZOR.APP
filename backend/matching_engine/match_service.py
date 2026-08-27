from sqlalchemy.orm import Session

from backend.models.swipe import Swipe
from backend.models.match import Match


class MatchService:

    @staticmethod
    def check_match(
        db: Session,
        user_id: int,
        target_id: int,
    ):

        reverse_like = (
            db.query(Swipe)
            .filter(
                Swipe.user_id == target_id,
                Swipe.target_user_id == user_id,
                Swipe.action.in_(
                    ["like", "super_like"]
                ),
            )
            .first()
        )

        if not reverse_like:
            return None

        existing = (
            db.query(Match)
            .filter(
                (
                    (Match.user_a_id == user_id) &
                    (Match.user_b_id == target_id)
                )
                |
                (
                    (Match.user_a_id == target_id) &
                    (Match.user_b_id == user_id)
                )
            )
            .first()
        )

        if existing:
            return existing

        match = Match(
            user_a_id=user_id,
            user_b_id=target_id,
        )

        db.add(match)
        db.commit()
        db.refresh(match)

        return match