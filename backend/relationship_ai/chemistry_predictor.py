class ChemistryPredictor:

    def predict(
        self,
        compatibility_score: float,
        conversation_score: float
    ):

        score = (
            compatibility_score +
            conversation_score
        ) / 2

        if score >= 80:
            return "high"

        if score >= 60:
            return "medium"

        return "low"


chemistry_predictor = ChemistryPredictor()