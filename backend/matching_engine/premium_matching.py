class PremiumMatching:

    @staticmethod
    def adjust_score(
        score: float,
        is_premium: bool,
    ) -> float:

        if not is_premium:
            return score

        return score * 1.10