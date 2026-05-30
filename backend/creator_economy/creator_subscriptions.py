# backend/creator_economy/creator_subscriptions.py

from datetime import datetime
from typing import Dict, List
import uuid


class CreatorSubscriptions:
    """
    Creator Subscription Engine

    Features:

    - Monthly subscriptions
    - Annual subscriptions
    - Premium creator access
    - Subscription analytics
    - Renewal tracking
    - Revenue tracking
    - Active member management
    """

    def __init__(self):

        self.subscriptions = {}

    # ==================================================
    # CREATE SUBSCRIPTION
    # ==================================================

    def create_subscription(
        self,
        user_id: int,
        creator_id: int,
        tier_name: str,
        price: float,
        duration: str = "monthly"
    ) -> Dict:

        subscription_id = str(uuid.uuid4())

        subscription = {
            "subscription_id": subscription_id,
            "user_id": user_id,
            "creator_id": creator_id,
            "tier_name": tier_name,
            "price": price,
            "duration": duration,
            "status": "active",
            "created_at": datetime.utcnow().isoformat(),
            "renewal_enabled": True
        }

        self.subscriptions[
            subscription_id
        ] = subscription

        return subscription

    # ==================================================
    # CANCEL SUBSCRIPTION
    # ==================================================

    def cancel_subscription(
        self,
        subscription_id: str
    ) -> bool:

        if subscription_id not in self.subscriptions:
            return False

        self.subscriptions[
            subscription_id
        ]["status"] = "cancelled"

        return True

    # ==================================================
    # PAUSE SUBSCRIPTION
    # ==================================================

    def pause_subscription(
        self,
        subscription_id: str
    ) -> bool:

        if subscription_id not in self.subscriptions:
            return False

        self.subscriptions[
            subscription_id
        ]["status"] = "paused"

        return True

    # ==================================================
    # RESUME SUBSCRIPTION
    # ==================================================

    def resume_subscription(
        self,
        subscription_id: str
    ) -> bool:

        if subscription_id not in self.subscriptions:
            return False

        self.subscriptions[
            subscription_id
        ]["status"] = "active"

        return True

    # ==================================================
    # TOGGLE AUTO RENEW
    # ==================================================

    def toggle_auto_renew(
        self,
        subscription_id: str,
        enabled: bool
    ) -> bool:

        if subscription_id not in self.subscriptions:
            return False

        self.subscriptions[
            subscription_id
        ]["renewal_enabled"] = enabled

        return True

    # ==================================================
    # ACTIVE SUBSCRIBERS
    # ==================================================

    def active_subscribers(
        self,
        creator_id: int
    ) -> int:

        return len([
            subscription
            for subscription
            in self.subscriptions.values()
            if (
                subscription["creator_id"]
                == creator_id
                and
                subscription["status"]
                == "active"
            )
        ])

    # ==================================================
    # CREATOR SUBSCRIPTIONS
    # ==================================================

    def creator_subscriptions(
        self,
        creator_id: int
    ) -> List[Dict]:

        return [
            subscription
            for subscription
            in self.subscriptions.values()
            if subscription["creator_id"]
            == creator_id
        ]

    # ==================================================
    # USER SUBSCRIPTIONS
    # ==================================================

    def user_subscriptions(
        self,
        user_id: int
    ) -> List[Dict]:

        return [
            subscription
            for subscription
            in self.subscriptions.values()
            if subscription["user_id"]
            == user_id
        ]

    # ==================================================
    # MONTHLY REVENUE
    # ==================================================

    def monthly_revenue(
        self,
        creator_id: int
    ) -> float:

        total = 0

        for subscription in self.subscriptions.values():

            if (
                subscription["creator_id"]
                == creator_id
                and
                subscription["status"]
                == "active"
            ):

                total += subscription["price"]

        return round(total, 2)

    # ==================================================
    # ANNUAL REVENUE
    # ==================================================

    def annual_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            self.monthly_revenue(
                creator_id
            ) * 12,
            2
        )

    # ==================================================
    # TOP SUBSCRIBED CREATORS
    # ==================================================

    def top_creators(
        self,
        limit: int = 25
    ):

        creators = {}

        for subscription in (
            self.subscriptions.values()
        ):

            if (
                subscription["status"]
                != "active"
            ):
                continue

            creator_id = (
                subscription["creator_id"]
            )

            creators.setdefault(
                creator_id,
                0
            )

            creators[
                creator_id
            ] += 1

        return sorted(
            creators.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

    # ==================================================
    # SUBSCRIPTION ANALYTICS
    # ==================================================

    def analytics(
        self,
        creator_id: int
    ) -> Dict:

        subscriptions = (
            self.creator_subscriptions(
                creator_id
            )
        )

        active = len([
            s
            for s in subscriptions
            if s["status"] == "active"
        ])

        cancelled = len([
            s
            for s in subscriptions
            if s["status"] == "cancelled"
        ])

        paused = len([
            s
            for s in subscriptions
            if s["status"] == "paused"
        ])

        return {

            "creator_id":
                creator_id,

            "total_subscriptions":
                len(subscriptions),

            "active_subscriptions":
                active,

            "cancelled_subscriptions":
                cancelled,

            "paused_subscriptions":
                paused,

            "monthly_revenue":
                self.monthly_revenue(
                    creator_id
                ),

            "annual_revenue":
                self.annual_revenue(
                    creator_id
                )
        }

    # ==================================================
    # CREATOR DASHBOARD
    # ==================================================

    def dashboard(
        self,
        creator_id: int
    ) -> Dict:

        return {

            "subscribers":
                self.active_subscribers(
                    creator_id
                ),

            "monthly_revenue":
                self.monthly_revenue(
                    creator_id
                ),

            "annual_revenue":
                self.annual_revenue(
                    creator_id
                ),

            "analytics":
                self.analytics(
                    creator_id
                )
        }


creator_subscriptions = CreatorSubscriptions()