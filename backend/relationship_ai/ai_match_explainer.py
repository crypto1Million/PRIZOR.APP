class AIMatchExplainer:

    def explain(
        self,
        common_interests: int,
        common_fandoms: int
    ):

        return (
            f"You share "
            f"{common_interests} interests "
            f"and "
            f"{common_fandoms} fandoms."
        )


ai_match_explainer = AIMatchExplainer()