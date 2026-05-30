# backend/creator_economy/creator_revenue.py

from datetime import datetime
from typing import Dict, List
import uuid


class CreatorRevenue:
    """
    Revenue Engine

    Tracks:

    - subscriptions
    - tips
    - sponsorships
    - merchandise
    - digital drops
    - affiliate revenue
    - event revenue

    Production-ready revenue aggregation layer.
    """

    def __init__(self):

        self.transactions = {}

    # ==================================================
    # RECORD REVENUE
    # ==================================================

    def record_revenue(
        self,
        creator_id: int,
        source: str,
        amount: float,
        reference_id: str = None
    ) -> Dict:

        revenue_id = str(uuid.uuid4())

        revenue = {
            "revenue_id": revenue_id,
            "creator_id": creator_id,
            "source": source,
            "amount": amount,
            "reference_id": reference_id,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.transactions[revenue_id] = revenue

        return revenue

    # ==================================================
    # CREATOR REVENUE
    # ==================================================

    def creator_revenue(
        self,
        creator_id: int
    ) -> List[Dict]:

        return [
            tx
            for tx in self.transactions.values()
            if tx["creator_id"] == creator_id
        ]

    # ==================================================
    # TOTAL REVENUE
    # ==================================================

    def total_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
            ),
            2
        )

    # ==================================================
    # REVENUE BY SOURCE
    # ==================================================

    def revenue_by_source(
        self,
        creator_id: int
    ) -> Dict:

        data = {}

        for tx in self.transactions.values():

            if tx["creator_id"] != creator_id:
                continue

            source = tx["source"]

            data.setdefault(
                source,
                0
            )

            data[source] += tx["amount"]

        return data

    # ==================================================
    # SUBSCRIPTION REVENUE
    # ==================================================

    def subscription_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "subscription"
            ),
            2
        )

    # ==================================================
    # SPONSORSHIP REVENUE
    # ==================================================

    def sponsorship_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "sponsorship"
            ),
            2
        )

    # ==================================================
    # MERCH REVENUE
    # ==================================================

    def merchandise_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "merchandise"
            ),
            2
        )

    # ==================================================
    # TIP REVENUE
    # ==================================================

    def tip_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "tip"
            ),
            2
        )

    # ==================================================
    # DIGITAL DROP REVENUE
    # ==================================================

    def digital_drop_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "digital_drop"
            ),
            2
        )

    # ==================================================
    # EVENT REVENUE
    # ==================================================

    def event_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "event"
            ),
            2
        )

    # ==================================================
    # AFFILIATE REVENUE
    # ==================================================

    def affiliate_revenue(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                tx["amount"]
                for tx in self.transactions.values()
                if tx["creator_id"] == creator_id
                and tx["source"] == "affiliate"
            ),
            2
        )

    # ==================================================
    # MONTHLY REVENUE
    # ==================================================

    def monthly_revenue(
        self,
        creator_id: int,
        month: int,
        year: int
    ) -> float:

        total = 0

        for tx in self.transactions.values():

            if tx["creator_id"] != creator_id:
                continue

            timestamp = datetime.fromisoformat(
                tx["timestamp"]
            )

            if (
                timestamp.month == month
                and
                timestamp.year == year
            ):
                total += tx["amount"]

        return round(total, 2)

    # ==================================================
    # CREATOR DASHBOARD
    # ==================================================

    def dashboard(
        self,
        creator_id: int
    ) -> Dict:

        return {
            "total_revenue":
                self.total_revenue(
                    creator_id
                ),

            "subscriptions":
                self.subscription_revenue(
                    creator_id
                ),

            "sponsorships":
                self.sponsorship_revenue(
                    creator_id
                ),

            "tips":
                self.tip_revenue(
                    creator_id
                ),

            "merchandise":
                self.merchandise_revenue(
                    creator_id
                ),

            "digital_drops":
                self.digital_drop_revenue(
                    creator_id
                ),

            "events":
                self.event_revenue(
                    creator_id
                ),

            "affiliates":
                self.affiliate_revenue(
                    creator_id
                )
        }


creator_revenue = CreatorRevenue()