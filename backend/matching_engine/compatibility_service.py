from sqlalchemy.orm import Session

from backend.matching_engine.interest_service import (
    InterestService
)


class CompatibilityService:

    @staticmethod
    def calculate(
        db: Session,
        user_id: int,
        candidate_id: int,
    ) -> float:

        # Replace with the actual AI/ML
        # compatibility model later.

        user_interests = set()
        candidate_interests = set()

        interest_score = (
            InterestService.calculate(
                user_interests,
                candidate_interests,
            )
        )

        return interest_score * 100