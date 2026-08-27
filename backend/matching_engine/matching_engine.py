from sqlalchemy.orm import Session

from backend.matching_engine.candidate_service import CandidateService
from backend.matching_engine.compatibility_service import CompatibilityService
from backend.matching_engine.scoring.final_score import FinalScore


class MatchingEngine:

    def __init__(self, db: Session):
        self.db = db

    def generate_matches(
        self,
        user_id: int,
        limit: int = 20,
    ):

        candidates = CandidateService.get_candidates(
            self.db,
            user_id=user_id,
            limit=500,
        )

        ranked = []

        for candidate in candidates:

            compatibility = (
                CompatibilityService.calculate(
                    self.db,
                    user_id,
                    candidate.id,
                )
            )

            score = FinalScore.calculate(
                compatibility=compatibility,
                candidate=candidate,
            )

            ranked.append(
                {
                    "user": candidate,
                    "score": score,
                }
            )

        ranked.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return ranked[:limit]