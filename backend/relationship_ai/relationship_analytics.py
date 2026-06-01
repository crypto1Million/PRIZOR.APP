class RelationshipAnalytics:

    def summary(
        self,
        compatibility_score,
        health_score,
        chemistry
    ):

        return {
            "compatibility_score":
                compatibility_score,

            "relationship_health":
                health_score,

            "chemistry":
                chemistry
        }


relationship_analytics = RelationshipAnalytics()