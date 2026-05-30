# backend/creator_economy/creator_memberships.py

from datetime import datetime
from typing import Dict, List, Optional


class CreatorMemberships:
    """
    Creator Membership Engine

    Handles:
    - Membership tiers
    - Membership enrollment
    - Membership benefits
    - Membership validation
    - Membership expiration
    """

    DEFAULT_TIERS = [
        "FREE",
        "BRONZE",
        "SILVER",
        "GOLD",
        "VIP"
    ]

    def __init__(self):
        self.memberships = {}

    # =====================================================
    # CREATE MEMBERSHIP TIER
    # =====================================================

    def create_membership_tier(
        self,
        creator_id: int,
        tier_name: str,
        price: float,
        benefits: List[str]
    ) -> Dict:

        return {
            "creator_id": creator_id,
            "tier_name": tier_name.upper(),
            "price": price,
            "benefits": benefits,
            "created_at": datetime.utcnow().isoformat()
        }

    # =====================================================
    # SUBSCRIBE USER
    # =====================================================

    def subscribe_user(
        self,
        user_id: int,
        creator_id: int,
        tier_name: str
    ) -> Dict:

        membership = {
            "user_id": user_id,
            "creator_id": creator_id,
            "tier": tier_name.upper(),
            "active": True,
            "subscribed_at": datetime.utcnow().isoformat()
        }

        self.memberships[(user_id, creator_id)] = membership

        return membership

    # =====================================================
    # CANCEL MEMBERSHIP
    # =====================================================

    def cancel_membership(
        self,
        user_id: int,
        creator_id: int
    ) -> Dict:

        key = (user_id, creator_id)

        if key not in self.memberships:
            return {
                "success": False,
                "message": "Membership not found"
            }

        self.memberships[key]["active"] = False

        return {
            "success": True,
            "message": "Membership cancelled"
        }

    # =====================================================
    # CHECK MEMBERSHIP STATUS
    # =====================================================

    def membership_status(
        self,
        user_id: int,
        creator_id: int
    ) -> Dict:

        return self.memberships.get(
            (user_id, creator_id),
            {
                "active": False
            }
        )

    # =====================================================
    # VERIFY ACCESS
    # =====================================================

    def has_access(
        self,
        user_id: int,
        creator_id: int,
        required_tier: str
    ) -> bool:

        membership = self.memberships.get(
            (user_id, creator_id)
        )

        if not membership:
            return False

        if not membership["active"]:
            return False

        user_tier = membership["tier"]

        try:
            return (
                self.DEFAULT_TIERS.index(user_tier)
                >=
                self.DEFAULT_TIERS.index(
                    required_tier.upper()
                )
            )

        except ValueError:
            return False

    # =====================================================
    # GET USER MEMBERSHIPS
    # =====================================================

    def get_user_memberships(
        self,
        user_id: int
    ) -> List[Dict]:

        results = []

        for membership in self.memberships.values():

            if membership["user_id"] == user_id:
                results.append(membership)

        return results

    # =====================================================
    # GET CREATOR SUBSCRIBERS
    # =====================================================

    def get_creator_subscribers(
        self,
        creator_id: int
    ) -> List[Dict]:

        results = []

        for membership in self.memberships.values():

            if membership["creator_id"] == creator_id:
                results.append(membership)

        return results

    # =====================================================
    # COUNT ACTIVE MEMBERS
    # =====================================================

    def active_member_count(
        self,
        creator_id: int
    ) -> int:

        count = 0

        for membership in self.memberships.values():

            if (
                membership["creator_id"] == creator_id
                and membership["active"]
            ):
                count += 1

        return count

    # =====================================================
    # MEMBERSHIP REVENUE ESTIMATE
    # =====================================================

    def estimate_monthly_revenue(
        self,
        active_members: int,
        tier_price: float
    ) -> float:

        return round(
            active_members * tier_price,
            2
        )


creator_memberships = CreatorMemberships()