# backend/creator_economy/creator_sponsorships.py

from datetime import datetime
from typing import Dict, List
import uuid


class CreatorSponsorships:
    """
    Creator Sponsorship Engine

    Supports:

    - Brand sponsorships
    - Campaign partnerships
    - Sponsored posts
    - Contract tracking
    - Deliverable tracking
    - Sponsor analytics
    - Creator earnings
    """

    def __init__(self):

        self.sponsorships = {}
        self.deliverables = {}
        self.payments = {}

    # ==================================================
    # CREATE SPONSORSHIP
    # ==================================================

    def create_sponsorship(
        self,
        creator_id: int,
        brand_id: int,
        brand_name: str,
        campaign_name: str,
        payout: float
    ) -> Dict:

        sponsorship_id = str(uuid.uuid4())

        sponsorship = {
            "sponsorship_id": sponsorship_id,
            "creator_id": creator_id,
            "brand_id": brand_id,
            "brand_name": brand_name,
            "campaign_name": campaign_name,
            "payout": payout,
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }

        self.sponsorships[
            sponsorship_id
        ] = sponsorship

        self.deliverables[
            sponsorship_id
        ] = []

        self.payments[
            sponsorship_id
        ] = []

        return sponsorship

    # ==================================================
    # ADD DELIVERABLE
    # ==================================================

    def add_deliverable(
        self,
        sponsorship_id: str,
        deliverable_type: str,
        description: str
    ) -> Dict:

        deliverable = {
            "deliverable_id": str(uuid.uuid4()),
            "type": deliverable_type,
            "description": description,
            "completed": False,
            "created_at": datetime.utcnow().isoformat()
        }

        self.deliverables[
            sponsorship_id
        ].append(deliverable)

        return deliverable

    # ==================================================
    # COMPLETE DELIVERABLE
    # ==================================================

    def complete_deliverable(
        self,
        sponsorship_id: str,
        deliverable_id: str
    ) -> bool:

        items = self.deliverables.get(
            sponsorship_id,
            []
        )

        for item in items:

            if item["deliverable_id"] == deliverable_id:

                item["completed"] = True
                return True

        return False

    # ==================================================
    # RECORD PAYMENT
    # ==================================================

    def record_payment(
        self,
        sponsorship_id: str,
        amount: float
    ) -> Dict:

        payment = {
            "payment_id": str(uuid.uuid4()),
            "amount": amount,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.payments[
            sponsorship_id
        ].append(payment)

        return payment

    # ==================================================
    # TOTAL PAID
    # ==================================================

    def total_paid(
        self,
        sponsorship_id: str
    ) -> float:

        return round(
            sum(
                payment["amount"]
                for payment
                in self.payments.get(
                    sponsorship_id,
                    []
                )
            ),
            2
        )

    # ==================================================
    # OUTSTANDING BALANCE
    # ==================================================

    def outstanding_balance(
        self,
        sponsorship_id: str
    ) -> float:

        sponsorship = self.sponsorships.get(
            sponsorship_id
        )

        if not sponsorship:
            return 0.0

        payout = sponsorship["payout"]

        paid = self.total_paid(
            sponsorship_id
        )

        return round(
            payout - paid,
            2
        )

    # ==================================================
    # SPONSORSHIP ANALYTICS
    # ==================================================

    def analytics(
        self,
        sponsorship_id: str
    ) -> Dict:

        deliverables = self.deliverables.get(
            sponsorship_id,
            []
        )

        completed = len(
            [
                d for d in deliverables
                if d["completed"]
            ]
        )

        total = len(deliverables)

        completion_rate = 0

        if total > 0:

            completion_rate = round(
                (completed / total) * 100,
                2
            )

        return {
            "sponsorship_id":
                sponsorship_id,

            "total_deliverables":
                total,

            "completed_deliverables":
                completed,

            "completion_rate":
                completion_rate,

            "paid":
                self.total_paid(
                    sponsorship_id
                ),

            "outstanding_balance":
                self.outstanding_balance(
                    sponsorship_id
                )
        }

    # ==================================================
    # CREATOR SPONSORSHIPS
    # ==================================================

    def creator_sponsorships(
        self,
        creator_id: int
    ) -> List[Dict]:

        return [
            sponsorship
            for sponsorship
            in self.sponsorships.values()
            if sponsorship["creator_id"]
            == creator_id
        ]

    # ==================================================
    # BRAND SPONSORSHIPS
    # ==================================================

    def brand_sponsorships(
        self,
        brand_id: int
    ) -> List[Dict]:

        return [
            sponsorship
            for sponsorship
            in self.sponsorships.values()
            if sponsorship["brand_id"]
            == brand_id
        ]

    # ==================================================
    # CLOSE SPONSORSHIP
    # ==================================================

    def close_sponsorship(
        self,
        sponsorship_id: str
    ) -> bool:

        if sponsorship_id not in self.sponsorships:
            return False

        self.sponsorships[
            sponsorship_id
        ]["status"] = "completed"

        return True

    # ==================================================
    # TOP SPONSORS
    # ==================================================

    def top_sponsors(
        self,
        limit: int = 20
    ):

        sponsors = {}

        for sponsorship in self.sponsorships.values():

            brand = sponsorship["brand_name"]

            sponsors.setdefault(
                brand,
                0
            )

            sponsors[
                brand
            ] += sponsorship["payout"]

        return sorted(
            sponsors.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]


creator_sponsorships = CreatorSponsorships()