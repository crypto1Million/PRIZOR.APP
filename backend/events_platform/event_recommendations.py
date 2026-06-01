from typing import List, Dict


class EventRecommendations:

    def recommend_for_user(
        self,
        user_id: int
    ) -> List[Dict]:

        return []

    def recommend_by_fandom(
        self,
        fandom: str
    ) -> List[Dict]:

        return []

    def recommend_by_location(
        self,
        location: str
    ) -> List[Dict]:

        return []


event_recommendations = EventRecommendations()