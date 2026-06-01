class RelationshipRisk:

    def detect(
        self,
        days_without_reply: int
    ):

        if days_without_reply >= 7:
            return "high"

        if days_without_reply >= 3:
            return "medium"

        return "low"


relationship_risk = RelationshipRisk()