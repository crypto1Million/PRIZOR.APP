class BusinessInsights:

    def generate(
        self,
        engagement_growth: float
    ):

        if engagement_growth > 20:
            return "Campaign performance is growing strongly."

        return "Campaign performance is stable."


business_insights = BusinessInsights()