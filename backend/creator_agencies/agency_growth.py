class AgencyGrowth:

    def growth_score(
        self,
        agency_id: int
    ):

        return {
            "agency_id": agency_id,
            "growth_score": 0
        }

    def recommend_creators(
        self,
        agency_id: int
    ):

        return []


agency_growth = AgencyGrowth()