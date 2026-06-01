class CompatibilityEngine:

    def calculate_score(
        self,
        common_interests: int,
        common_fandoms: int,
        communication_score: float
    ):

        score = (
            common_interests * 10 +
            common_fandoms * 15 +
            communication_score
        )

        return min(score, 100)


compatibility_engine = CompatibilityEngine()