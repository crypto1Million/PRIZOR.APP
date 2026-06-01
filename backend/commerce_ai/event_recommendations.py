class CommerceEventRecommendations:

    def recommend(
        self,
        user_id: int
    ):
        return []

    def nearby_events(
        self,
        location: str
    ):
        return []

    def fandom_events(
        self,
        fandom: str
    ):
        return []


event_recommendations = CommerceEventRecommendations()