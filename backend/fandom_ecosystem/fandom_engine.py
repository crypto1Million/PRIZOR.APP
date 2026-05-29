# backend/fandom_ecosystem/fandom_engine.py

from backend.fandom_ecosystem.tribe_classifier import TribeClassifier
from backend.fandom_ecosystem.fandom_matcher import FandomMatcher
from backend.fandom_ecosystem.fandom_recommendations import (
    FandomRecommendationEngine,
)


class FandomEngine:

    def __init__(self):

        self.classifier = TribeClassifier()
        self.matcher = FandomMatcher()
        self.recommendations = FandomRecommendationEngine()

    def analyze_user(self, user_profile: dict):

        tribe = self.classifier.classify(user_profile)

        matches = self.matcher.find_matches(
            tribe=tribe,
            interests=user_profile.get("interests", [])
        )

        recommendations = self.recommendations.generate(
            tribe=tribe,
            interests=user_profile.get("interests", [])
        )

        return {
            "tribe": tribe,
            "matches": matches,
            "recommendations": recommendations
        }