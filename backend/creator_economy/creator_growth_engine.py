# backend/creator_economy/creator_growth_engine.py

from datetime import datetime
from typing import Dict, List
import uuid


class CreatorGrowthEngine:
    """
    Creator Growth Engine

    Features:

    - creator growth scoring
    - growth recommendations
    - milestone tracking
    - engagement optimization
    - revenue growth tracking
    - subscriber growth tracking
    - creator health score
    - creator progression levels
    """

    def __init__(self):

        self.creator_metrics = {}
        self.milestones = {}

    # ==================================================
    # REGISTER CREATOR
    # ==================================================

    def register_creator(
        self,
        creator_id: int
    ):

        if creator_id not in self.creator_metrics:

            self.creator_metrics[
                creator_id
            ] = {

                "followers": 0,
                "subscribers": 0,
                "revenue": 0.0,
                "engagement": 0,
                "growth_score": 0,
                "level": 1,

                "created_at":
                    datetime.utcnow().isoformat()
            }

            self.milestones[
                creator_id
            ] = []

    # ==================================================
    # UPDATE FOLLOWERS
    # ==================================================

    def update_followers(
        self,
        creator_id: int,
        count: int
    ):

        self.register_creator(
            creator_id
        )

        self.creator_metrics[
            creator_id
        ]["followers"] = count

        self.calculate_growth_score(
            creator_id
        )

    # ==================================================
    # UPDATE SUBSCRIBERS
    # ==================================================

    def update_subscribers(
        self,
        creator_id: int,
        count: int
    ):

        self.register_creator(
            creator_id
        )

        self.creator_metrics[
            creator_id
        ]["subscribers"] = count

        self.calculate_growth_score(
            creator_id
        )

    # ==================================================
    # UPDATE REVENUE
    # ==================================================

    def update_revenue(
        self,
        creator_id: int,
        revenue: float
    ):

        self.register_creator(
            creator_id
        )

        self.creator_metrics[
            creator_id
        ]["revenue"] = revenue

        self.calculate_growth_score(
            creator_id
        )

    # ==================================================
    # UPDATE ENGAGEMENT
    # ==================================================

    def update_engagement(
        self,
        creator_id: int,
        engagement: int
    ):

        self.register_creator(
            creator_id
        )

        self.creator_metrics[
            creator_id
        ]["engagement"] = engagement

        self.calculate_growth_score(
            creator_id
        )

    # ==================================================
    # CALCULATE GROWTH SCORE
    # ==================================================

    def calculate_growth_score(
        self,
        creator_id: int
    ):

        creator = self.creator_metrics[
            creator_id
        ]

        score = (

            creator["followers"] * 0.10

            +

            creator["subscribers"] * 3

            +

            creator["engagement"] * 0.50

            +

            creator["revenue"] * 0.05

        )

        creator["growth_score"] = round(
            score,
            2
        )

        creator["level"] = self.calculate_level(
            score
        )

    # ==================================================
    # CREATOR LEVEL
    # ==================================================

    def calculate_level(
        self,
        score: float
    ) -> int:

        if score >= 100000:
            return 10

        if score >= 50000:
            return 9

        if score >= 25000:
            return 8

        if score >= 10000:
            return 7

        if score >= 5000:
            return 6

        if score >= 2500:
            return 5

        if score >= 1000:
            return 4

        if score >= 500:
            return 3

        if score >= 100:
            return 2

        return 1

    # ==================================================
    # ADD MILESTONE
    # ==================================================

    def add_milestone(
        self,
        creator_id: int,
        title: str
    ):

        milestone = {

            "id":
                str(uuid.uuid4()),

            "title":
                title,

            "timestamp":
                datetime.utcnow().isoformat()
        }

        self.milestones[
            creator_id
        ].append(
            milestone
        )

        return milestone

    # ==================================================
    # GROWTH RECOMMENDATIONS
    # ==================================================

    def recommendations(
        self,
        creator_id: int
    ) -> List[str]:

        creator = self.creator_metrics[
            creator_id
        ]

        suggestions = []

        if creator["engagement"] < 100:

            suggestions.append(
                "Increase posting frequency."
            )

        if creator["subscribers"] < 50:

            suggestions.append(
                "Launch premium memberships."
            )

        if creator["followers"] < 1000:

            suggestions.append(
                "Collaborate with creators."
            )

        if creator["revenue"] < 500:

            suggestions.append(
                "Enable monetization tools."
            )

        if not suggestions:

            suggestions.append(
                "Growth trajectory is healthy."
            )

        return suggestions

    # ==================================================
    # CREATOR HEALTH SCORE
    # ==================================================

    def health_score(
        self,
        creator_id: int
    ) -> Dict:

        creator = self.creator_metrics[
            creator_id
        ]

        score = min(
            creator["growth_score"] / 100,
            100
        )

        return {

            "creator_id":
                creator_id,

            "health_score":
                round(score, 2),

            "level":
                creator["level"]
        }

    # ==================================================
    # TOP GROWING CREATORS
    # ==================================================

    def top_creators(
        self,
        limit: int = 50
    ):

        creators = []

        for creator_id, metrics in (
            self.creator_metrics.items()
        ):

            creators.append({

                "creator_id":
                    creator_id,

                "growth_score":
                    metrics["growth_score"],

                "level":
                    metrics["level"]
            })

        creators.sort(
            key=lambda x: x["growth_score"],
            reverse=True
        )

        return creators[:limit]

    # ==================================================
    # CREATOR DASHBOARD
    # ==================================================

    def dashboard(
        self,
        creator_id: int
    ) -> Dict:

        creator = self.creator_metrics[
            creator_id
        ]

        return {

            "creator_id":
                creator_id,

            "followers":
                creator["followers"],

            "subscribers":
                creator["subscribers"],

            "revenue":
                creator["revenue"],

            "engagement":
                creator["engagement"],

            "growth_score":
                creator["growth_score"],

            "level":
                creator["level"],

            "recommendations":
                self.recommendations(
                    creator_id
                ),

            "health":
                self.health_score(
                    creator_id
                ),

            "milestones":
                self.milestones.get(
                    creator_id,
                    []
                )
        }


creator_growth_engine = (
    CreatorGrowthEngine()
)