class BoostService:

    @staticmethod
    def apply(
        score: float,
        boost_multiplier: float = 1.0,
    ) -> float:

        if boost_multiplier < 1:
            boost_multiplier = 1

        return score * boost_multiplier