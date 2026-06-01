class RelationshipInsights:

    def analyze(
        self,
        message_count: int,
        reply_rate: float
    ):

        if reply_rate > 0.8:
            return "Strong engagement"

        if reply_rate > 0.5:
            return "Moderate engagement"

        return "Weak engagement"


relationship_insights = RelationshipInsights()