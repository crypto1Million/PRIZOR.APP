class RelationshipScoring:

    def calculate_health(
        self,
        engagement: float,
        reciprocity: float,
        consistency: float
    ):

        score = (
            engagement +
            reciprocity +
            consistency
        ) / 3

        return round(score, 2)


relationship_scoring = RelationshipScoring()