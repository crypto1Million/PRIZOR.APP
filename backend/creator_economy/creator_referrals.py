# backend/creator_economy/creator_referrals.py

from datetime import datetime
from typing import Dict, List


class CreatorReferrals:
    """
    Creator Referral Engine

    Handles:
    - User referrals
    - Creator referrals
    - Referral rewards
    - Referral analytics
    """

    def __init__(self):
        self.referrals = []
        self.referral_rewards = {}

    # =====================================================
    # CREATE REFERRAL
    # =====================================================

    def create_referral(
        self,
        referrer_id: int,
        referred_id: int,
        referral_type: str = "user"
    ) -> Dict:

        referral = {
            "referrer_id": referrer_id,
            "referred_id": referred_id,
            "referral_type": referral_type,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }

        self.referrals.append(referral)

        return referral

    # =====================================================
    # APPROVE REFERRAL
    # =====================================================

    def approve_referral(
        self,
        referred_id: int,
        reward_amount: float = 10.0
    ) -> Dict:

        for referral in self.referrals:

            if referral["referred_id"] == referred_id:

                referral["status"] = "completed"

                referrer_id = referral["referrer_id"]

                self.referral_rewards.setdefault(
                    referrer_id,
                    0
                )

                self.referral_rewards[
                    referrer_id
                ] += reward_amount

                return {
                    "success": True,
                    "reward": reward_amount
                }

        return {
            "success": False,
            "message": "Referral not found"
        }

    # =====================================================
    # GET REFERRALS
    # =====================================================

    def get_referrals(
        self,
        referrer_id: int
    ) -> List[Dict]:

        return [
            referral
            for referral in self.referrals
            if referral["referrer_id"] == referrer_id
        ]

    # =====================================================
    # TOTAL REWARDS
    # =====================================================

    def total_rewards(
        self,
        referrer_id: int
    ) -> float:

        return round(
            self.referral_rewards.get(
                referrer_id,
                0
            ),
            2
        )

    # =====================================================
    # REFERRAL COUNT
    # =====================================================

    def referral_count(
        self,
        referrer_id: int
    ) -> int:

        return len(
            self.get_referrals(referrer_id)
        )

    # =====================================================
    # SUCCESSFUL REFERRALS
    # =====================================================

    def successful_referrals(
        self,
        referrer_id: int
    ) -> int:

        return len([
            referral
            for referral in self.referrals
            if referral["referrer_id"] == referrer_id
            and referral["status"] == "completed"
        ])

    # =====================================================
    # LEADERBOARD
    # =====================================================

    def referral_leaderboard(self):

        leaderboard = {}

        for referral in self.referrals:

            if referral["status"] != "completed":
                continue

            referrer_id = referral["referrer_id"]

            leaderboard.setdefault(
                referrer_id,
                0
            )

            leaderboard[referrer_id] += 1

        return sorted(
            leaderboard.items(),
            key=lambda x: x[1],
            reverse=True
        )


creator_referrals = CreatorReferrals()