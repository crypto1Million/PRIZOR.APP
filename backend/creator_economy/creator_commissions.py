# backend/creator_economy/creator_commissions.py

from datetime import datetime
from typing import Dict, List
import uuid


class CreatorCommissions:
    """
    Commission Engine

    Supports:

    - affiliate commissions
    - referral commissions
    - creator marketplace commissions
    - sponsorship commissions
    - brand partnership payouts
    - commission analytics
    """

    def __init__(self):

        self.commissions = {}

    # ==================================================
    # CREATE COMMISSION
    # ==================================================

    def create_commission(
        self,
        creator_id: int,
        amount: float,
        source: str,
        reference_id: str = None,
        percentage: float = 0.0
    ) -> Dict:

        commission_id = str(uuid.uuid4())

        commission = {
            "commission_id": commission_id,
            "creator_id": creator_id,
            "amount": amount,
            "source": source,
            "percentage": percentage,
            "reference_id": reference_id,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }

        self.commissions[
            commission_id
        ] = commission

        return commission

    # ==================================================
    # APPROVE COMMISSION
    # ==================================================

    def approve_commission(
        self,
        commission_id: str
    ) -> bool:

        if commission_id not in self.commissions:
            return False

        self.commissions[
            commission_id
        ]["status"] = "approved"

        return True

    # ==================================================
    # PAY COMMISSION
    # ==================================================

    def pay_commission(
        self,
        commission_id: str
    ) -> bool:

        if commission_id not in self.commissions:
            return False

        self.commissions[
            commission_id
        ]["status"] = "paid"

        self.commissions[
            commission_id
        ]["paid_at"] = (
            datetime.utcnow().isoformat()
        )

        return True

    # ==================================================
    # REJECT COMMISSION
    # ==================================================

    def reject_commission(
        self,
        commission_id: str
    ) -> bool:

        if commission_id not in self.commissions:
            return False

        self.commissions[
            commission_id
        ]["status"] = "rejected"

        return True

    # ==================================================
    # CREATOR COMMISSIONS
    # ==================================================

    def creator_commissions(
        self,
        creator_id: int
    ) -> List[Dict]:

        return [
            commission
            for commission
            in self.commissions.values()
            if commission["creator_id"]
            == creator_id
        ]

    # ==================================================
    # TOTAL COMMISSIONS
    # ==================================================

    def total_commissions(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                commission["amount"]
                for commission
                in self.commissions.values()
                if commission["creator_id"]
                == creator_id
            ),
            2
        )

    # ==================================================
    # PAID COMMISSIONS
    # ==================================================

    def paid_commissions(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                commission["amount"]
                for commission
                in self.commissions.values()
                if (
                    commission["creator_id"]
                    == creator_id
                    and
                    commission["status"]
                    == "paid"
                )
            ),
            2
        )

    # ==================================================
    # PENDING COMMISSIONS
    # ==================================================

    def pending_commissions(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                commission["amount"]
                for commission
                in self.commissions.values()
                if (
                    commission["creator_id"]
                    == creator_id
                    and
                    commission["status"]
                    == "pending"
                )
            ),
            2
        )

    # ==================================================
    # COMMISSION BY SOURCE
    # ==================================================

    def commission_by_source(
        self,
        creator_id: int
    ) -> Dict:

        result = {}

        for commission in self.commissions.values():

            if commission["creator_id"] != creator_id:
                continue

            source = commission["source"]

            result.setdefault(
                source,
                0
            )

            result[source] += commission["amount"]

        return result

    # ==================================================
    # TOP EARNING CREATORS
    # ==================================================

    def top_creators(
        self,
        limit: int = 20
    ):

        totals = {}

        for commission in self.commissions.values():

            creator_id = commission[
                "creator_id"
            ]

            totals.setdefault(
                creator_id,
                0
            )

            totals[
                creator_id
            ] += commission["amount"]

        return sorted(
            totals.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

    # ==================================================
    # COMMISSION ANALYTICS
    # ==================================================

    def analytics(
        self,
        creator_id: int
    ) -> Dict:

        creator_data = self.creator_commissions(
            creator_id
        )

        return {
            "creator_id":
                creator_id,

            "total_commissions":
                self.total_commissions(
                    creator_id
                ),

            "paid_commissions":
                self.paid_commissions(
                    creator_id
                ),

            "pending_commissions":
                self.pending_commissions(
                    creator_id
                ),

            "commission_count":
                len(
                    creator_data
                ),

            "sources":
                self.commission_by_source(
                    creator_id
                )
        }


creator_commissions = CreatorCommissions()