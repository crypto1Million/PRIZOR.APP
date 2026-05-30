# backend/lifestyle_commerce/commerce_recommendations.py

class CommerceRecommendations:

    def recommend(self, user_id: int):

        return [
            {
                "type": "product",
                "title": "Trending Apparel"
            }
        ]


commerce_recommendations = CommerceRecommendations()