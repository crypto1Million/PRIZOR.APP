class AgencyAnalytics:

    def creator_growth(
        self,
        creator_id: int
    ):

        return {
            "followers": 0,
            "engagement": 0
        }

    def agency_revenue(
        self,
        agency_id: int
    ):

        return {
            "revenue": 0
        }


agency_analytics = AgencyAnalytics()