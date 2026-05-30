# backend/creator_economy/creator_analytics.py

from datetime import datetime
from typing import Dict, List


class CreatorAnalytics:
    """
    Creator Analytics Engine

    Tracks:

    - Profile Views
    - Post Views
    - Likes
    - Comments
    - Shares
    - Followers
    - Revenue
    - Retention
    - Engagement Rate
    """

    def __init__(self):

        self.profile_views = {}
        self.post_views = {}

        self.likes = {}
        self.comments = {}
        self.shares = {}

        self.followers = {}
        self.revenue = {}

        self.events = []

    # =====================================================
    # EVENT LOGGER
    # =====================================================

    def log_event(
        self,
        creator_id: int,
        event_type: str,
        value: int = 1
    ) -> None:

        event = {
            "creator_id": creator_id,
            "event_type": event_type,
            "value": value,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(event)

    # =====================================================
    # PROFILE VIEW
    # =====================================================

    def track_profile_view(
        self,
        creator_id: int
    ) -> None:

        self.profile_views.setdefault(
            creator_id,
            0
        )

        self.profile_views[creator_id] += 1

        self.log_event(
            creator_id,
            "profile_view"
        )

    # =====================================================
    # POST VIEW
    # =====================================================

    def track_post_view(
        self,
        creator_id: int
    ) -> None:

        self.post_views.setdefault(
            creator_id,
            0
        )

        self.post_views[creator_id] += 1

        self.log_event(
            creator_id,
            "post_view"
        )

    # =====================================================
    # LIKE
    # =====================================================

    def track_like(
        self,
        creator_id: int
    ) -> None:

        self.likes.setdefault(
            creator_id,
            0
        )

        self.likes[creator_id] += 1

        self.log_event(
            creator_id,
            "like"
        )

    # =====================================================
    # COMMENT
    # =====================================================

    def track_comment(
        self,
        creator_id: int
    ) -> None:

        self.comments.setdefault(
            creator_id,
            0
        )

        self.comments[creator_id] += 1

        self.log_event(
            creator_id,
            "comment"
        )

    # =====================================================
    # SHARE
    # =====================================================

    def track_share(
        self,
        creator_id: int
    ) -> None:

        self.shares.setdefault(
            creator_id,
            0
        )

        self.shares[creator_id] += 1

        self.log_event(
            creator_id,
            "share"
        )

    # =====================================================
    # FOLLOWER COUNT
    # =====================================================

    def update_followers(
        self,
        creator_id: int,
        follower_count: int
    ) -> None:

        self.followers[
            creator_id
        ] = follower_count

    # =====================================================
    # REVENUE TRACKING
    # =====================================================

    def update_revenue(
        self,
        creator_id: int,
        amount: float
    ) -> None:

        self.revenue.setdefault(
            creator_id,
            0.0
        )

        self.revenue[
            creator_id
        ] += amount

    # =====================================================
    # ENGAGEMENT RATE
    # =====================================================

    def engagement_rate(
        self,
        creator_id: int
    ) -> float:

        views = self.post_views.get(
            creator_id,
            0
        )

        if views == 0:
            return 0.0

        interactions = (
            self.likes.get(creator_id, 0)
            +
            self.comments.get(creator_id, 0)
            +
            self.shares.get(creator_id, 0)
        )

        return round(
            (interactions / views) * 100,
            2
        )

    # =====================================================
    # AUDIENCE RETENTION
    # =====================================================

    def retention_score(
        self,
        returning_users: int,
        total_users: int
    ) -> float:

        if total_users == 0:
            return 0.0

        return round(
            (returning_users / total_users)
            * 100,
            2
        )

    # =====================================================
    # GROWTH RATE
    # =====================================================

    def growth_rate(
        self,
        previous_followers: int,
        current_followers: int
    ) -> float:

        if previous_followers == 0:
            return 100.0

        return round(
            (
                (
                    current_followers
                    -
                    previous_followers
                )
                /
                previous_followers
            )
            * 100,
            2
        )

    # =====================================================
    # REVENUE GROWTH
    # =====================================================

    def revenue_growth(
        self,
        previous_revenue: float,
        current_revenue: float
    ) -> float:

        if previous_revenue == 0:
            return 100.0

        return round(
            (
                (
                    current_revenue
                    -
                    previous_revenue
                )
                /
                previous_revenue
            )
            * 100,
            2
        )

    # =====================================================
    # CREATOR DASHBOARD
    # =====================================================

    def dashboard(
        self,
        creator_id: int
    ) -> Dict:

        return {
            "creator_id": creator_id,

            "profile_views":
                self.profile_views.get(
                    creator_id,
                    0
                ),

            "post_views":
                self.post_views.get(
                    creator_id,
                    0
                ),

            "likes":
                self.likes.get(
                    creator_id,
                    0
                ),

            "comments":
                self.comments.get(
                    creator_id,
                    0
                ),

            "shares":
                self.shares.get(
                    creator_id,
                    0
                ),

            "followers":
                self.followers.get(
                    creator_id,
                    0
                ),

            "engagement_rate":
                self.engagement_rate(
                    creator_id
                ),

            "revenue":
                round(
                    self.revenue.get(
                        creator_id,
                        0.0
                    ),
                    2
                )
        }

    # =====================================================
    # TOP CREATORS
    # =====================================================

    def top_creators_by_revenue(
        self,
        limit: int = 25
    ) -> List:

        return sorted(
            self.revenue.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

    # =====================================================
    # TOP CREATORS BY ENGAGEMENT
    # =====================================================

    def top_creators_by_engagement(
        self,
        limit: int = 25
    ):

        creators = []

        creator_ids = set(
            list(self.post_views.keys())
        )

        for creator_id in creator_ids:

            creators.append(
                (
                    creator_id,
                    self.engagement_rate(
                        creator_id
                    )
                )
            )

        return sorted(
            creators,
            key=lambda x: x[1],
            reverse=True
        )[:limit]


creator_analytics = CreatorAnalytics()