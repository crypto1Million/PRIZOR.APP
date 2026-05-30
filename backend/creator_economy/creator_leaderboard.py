# backend/creator_economy/creator_leaderboard.py

from datetime import datetime
from typing import Dict, List


class CreatorLeaderboard:
    """
    Creator Leaderboard Engine

    Tracks:

    - top creators
    - fastest growing creators
    - highest revenue creators
    - most subscribed creators
    - highest engagement creators
    - trending creators
    - fandom rankings

    Used for:
    Discover page
    Rankings page
    Creator ecosystem
    """

    def __init__(self):

        self.creator_scores = {}

    # ==================================================
    # REGISTER CREATOR
    # ==================================================

    def register_creator(
        self,
        creator_id: int
    ):

        if creator_id not in self.creator_scores:

            self.creator_scores[
                creator_id
            ] = {
                "revenue": 0.0,
                "followers": 0,
                "subscribers": 0,
                "engagement": 0,
                "likes": 0,
                "shares": 0,
                "comments": 0,
                "score": 0,
                "updated_at":
                    datetime.utcnow().isoformat()
            }

    # ==================================================
    # UPDATE REVENUE
    # ==================================================

    def update_revenue(
        self,
        creator_id: int,
        amount: float
    ):

        self.register_creator(
            creator_id
        )

        self.creator_scores[
            creator_id
        ]["revenue"] += amount

        self.calculate_score(
            creator_id
        )

    # ==================================================
    # UPDATE FOLLOWERS
    # ==================================================

    def update_followers(
        self,
        creator_id: int,
        followers: int
    ):

        self.register_creator(
            creator_id
        )

        self.creator_scores[
            creator_id
        ]["followers"] = followers

        self.calculate_score(
            creator_id
        )

    # ==================================================
    # UPDATE SUBSCRIBERS
    # ==================================================

    def update_subscribers(
        self,
        creator_id: int,
        subscribers: int
    ):

        self.register_creator(
            creator_id
        )

        self.creator_scores[
            creator_id
        ]["subscribers"] = subscribers

        self.calculate_score(
            creator_id
        )

    # ==================================================
    # UPDATE ENGAGEMENT
    # ==================================================

    def update_engagement(
        self,
        creator_id: int,
        likes: int = 0,
        comments: int = 0,
        shares: int = 0
    ):

        self.register_creator(
            creator_id
        )

        creator = self.creator_scores[
            creator_id
        ]

        creator["likes"] += likes
        creator["comments"] += comments
        creator["shares"] += shares

        creator["engagement"] = (
            creator["likes"]
            +
            creator["comments"] * 3
            +
            creator["shares"] * 5
        )

        self.calculate_score(
            creator_id
        )

    # ==================================================
    # LEADERBOARD SCORE
    # ==================================================

    def calculate_score(
        self,
        creator_id: int
    ):

        creator = self.creator_scores[
            creator_id
        ]

        score = (

            creator["revenue"] * 0.30

            +

            creator["followers"] * 0.10

            +

            creator["subscribers"] * 2

            +

            creator["engagement"] * 0.50

        )

        creator["score"] = round(
            score,
            2
        )

        creator["updated_at"] = (
            datetime.utcnow().isoformat()
        )

    # ==================================================
    # GLOBAL LEADERBOARD
    # ==================================================

    def leaderboard(
        self,
        limit: int = 100
    ) -> List[Dict]:

        creators = []

        for creator_id, data in (
            self.creator_scores.items()
        ):

            creators.append({
                "creator_id":
                    creator_id,

                "score":
                    data["score"],

                "revenue":
                    data["revenue"],

                "followers":
                    data["followers"],

                "subscribers":
                    data["subscribers"],

                "engagement":
                    data["engagement"]
            })

        creators.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return creators[:limit]

    # ==================================================
    # TOP REVENUE
    # ==================================================

    def top_revenue(
        self,
        limit: int = 50
    ):

        return sorted(
            self.creator_scores.items(),
            key=lambda x: x[1]["revenue"],
            reverse=True
        )[:limit]

    # ==================================================
    # TOP SUBSCRIBERS
    # ==================================================

    def top_subscribers(
        self,
        limit: int = 50
    ):

        return sorted(
            self.creator_scores.items(),
            key=lambda x: x[1]["subscribers"],
            reverse=True
        )[:limit]

    # ==================================================
    # TOP ENGAGEMENT
    # ==================================================

    def top_engagement(
        self,
        limit: int = 50
    ):

        return sorted(
            self.creator_scores.items(),
            key=lambda x: x[1]["engagement"],
            reverse=True
        )[:limit]

    # ==================================================
    # TRENDING CREATORS
    # ==================================================

    def trending_creators(
        self,
        limit: int = 25
    ):

        creators = []

        for creator_id, data in (
            self.creator_scores.items()
        ):

            trending_score = (

                data["engagement"] * 0.6

                +

                data["subscribers"] * 0.3

                +

                data["shares"] * 0.1

            )

            creators.append({
                "creator_id":
                    creator_id,

                "trending_score":
                    round(
                        trending_score,
                        2
                    )
            })

        creators.sort(
            key=lambda x: x["trending_score"],
            reverse=True
        )

        return creators[:limit]

    # ==================================================
    # CREATOR RANK
    # ==================================================

    def creator_rank(
        self,
        creator_id: int
    ):

        ranking = self.leaderboard()

        for position, creator in enumerate(
            ranking,
            start=1
        ):

            if (
                creator["creator_id"]
                == creator_id
            ):

                return {
                    "rank":
                        position,

                    "creator_id":
                        creator_id,

                    "score":
                        creator["score"]
                }

        return None


creator_leaderboard = CreatorLeaderboard()