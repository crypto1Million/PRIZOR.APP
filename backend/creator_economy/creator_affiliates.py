# backend/creator_economy/creator_affiliates.py

from datetime import datetime
from typing import Dict, List


class CreatorAffiliates:
    """
    Creator Affiliate Engine

    Handles:
    - Affiliate links
    - Creator partnerships
    - Commission tracking
    - Affiliate performance
    """

    def __init__(self):
        self.affiliates = {}
        self.sales = []

    # ==========================================
    # CREATE AFFILIATE
    # ==========================================

    def create_affiliate(
        self,
        creator_id: int,
        brand_id: int,
        commission_rate: float
    ) -> Dict:

        affiliate = {
            "creator_id": creator_id,
            "brand_id": brand_id,
            "commission_rate": commission_rate,
            "created_at": datetime.utcnow().isoformat(),
            "active": True
        }

        key = f"{creator_id}_{brand_id}"

        self.affiliates[key] = affiliate

        return affiliate

    # ==========================================
    # RECORD SALE
    # ==========================================

    def record_sale(
        self,
        creator_id: int,
        brand_id: int,
        order_value: float
    ) -> Dict:

        key = f"{creator_id}_{brand_id}"

        if key not in self.affiliates:
            return {
                "success": False,
                "message": "Affiliate not found"
            }

        affiliate = self.affiliates[key]

        commission = round(
            order_value * affiliate["commission_rate"] / 100,
            2
        )

        sale = {
            "creator_id": creator_id,
            "brand_id": brand_id,
            "order_value": order_value,
            "commission": commission,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.sales.append(sale)

        return {
            "success": True,
            "sale": sale
        }

    # ==========================================
    # CREATOR EARNINGS
    # ==========================================

    def creator_earnings(
        self,
        creator_id: int
    ) -> float:

        return round(
            sum(
                sale["commission"]
                for sale in self.sales
                if sale["creator_id"] == creator_id
            ),
            2
        )

    # ==========================================
    # CREATOR SALES
    # ==========================================

    def creator_sales(
        self,
        creator_id: int
    ) -> List[Dict]:

        return [
            sale
            for sale in self.sales
            if sale["creator_id"] == creator_id
        ]

    # ==========================================
    # TOP AFFILIATES
    # ==========================================

    def top_affiliates(self):

        creators = {}

        for sale in self.sales:

            creator_id = sale["creator_id"]

            creators.setdefault(
                creator_id,
                0
            )

            creators[creator_id] += sale["commission"]

        return sorted(
            creators.items(),
            key=lambda x: x[1],
            reverse=True
        )


creator_affiliates = CreatorAffiliates()