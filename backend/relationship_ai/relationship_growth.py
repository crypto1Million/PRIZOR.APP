class RelationshipGrowth:

    def suggest_activity(
        self,
        shared_interest: str
    ):

        return (
            f"Attend a community event "
            f"related to {shared_interest}"
        )


relationship_growth = RelationshipGrowth()