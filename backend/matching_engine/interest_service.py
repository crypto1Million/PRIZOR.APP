class InterestService:

    @staticmethod
    def calculate(
        user_interests: set,
        candidate_interests: set,
    ) -> float:

        if not user_interests:
            return 0.0

        if not candidate_interests:
            return 0.0

        intersection = (
            user_interests &
            candidate_interests
        )

        union = (
            user_interests |
            candidate_interests
        )

        if not union:
            return 0.0

        return len(intersection) / len(union)