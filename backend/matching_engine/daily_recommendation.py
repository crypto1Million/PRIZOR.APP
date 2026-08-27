from backend.matching_engine.matching_engine import (
    MatchingEngine
)


class DailyRecommendations:

    DAILY_LIMIT = 20

    @staticmethod
    def generate(
        db,
        user_id: int,
    ):

        engine = MatchingEngine(db)

        return engine.generate_matches(
            user_id=user_id,
            limit=DailyRecommendations.DAILY_LIMIT,
        )