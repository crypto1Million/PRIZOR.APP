from sqlalchemy.orm import Session

from backend.models.user import User


class CandidateService:

    @staticmethod
    def get_candidates(
        db: Session,
        user_id: int,
        limit: int = 500,
    ):

        return (
            db.query(User)
            .filter(User.id != user_id)
            .limit(limit)
            .all()
        )