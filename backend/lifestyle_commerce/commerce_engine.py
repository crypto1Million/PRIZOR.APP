# backend/lifestyle_commerce/commerce_engine.py

from .creator_store import CreatorStore
from .brand_marketplace import BrandMarketplace
from .commerce_recommendations import CommerceRecommendations


class CommerceEngine:

    def __init__(self):
        self.store = CreatorStore()
        self.marketplace = BrandMarketplace()
        self.recommendations = CommerceRecommendations()

    def get_user_commerce_dashboard(self, user_id: int):

        return {
            "stores": self.store.get_followed_creator_stores(user_id),
            "brands": self.marketplace.get_featured_brands(),
            "recommended": self.recommendations.recommend(user_id)
        }


commerce_engine = CommerceEngine()