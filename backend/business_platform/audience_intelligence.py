class AudienceIntelligence:

    def segment(
        self,
        age_group: str,
        interest: str
    ):

        return {
            "age_group": age_group,
            "interest": interest
        }


audience_intelligence = AudienceIntelligence()