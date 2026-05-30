# backend/creator_economy/creator_rewards.py

from datetime import datetime
from typing import Dict, List


class CreatorRewards:
    """
    Creator Rewards Engine

    Handles:
    - XP system
    - Achievement badges
    - Milestone rewards
    - Streak rewards
    - Creator levels
    """

    BADGES = {
        100: "Rising Creator",
        500: "Community Builder",
        1000: "Influencer",
        5000: "Trendsetter",
        10000: "Elite Creator",
        50000: "Legend Creator"
    }

    def __init__(self):
        self.creator_xp = {}
        self.creator_levels = {}
        self.creator_badges = {}
        self.reward_history = []

    # ==================================================
    # ADD XP
    # ==================================================

    def add_xp(
        self,
        creator_id: int,
        xp: int,
        reason: str
    ) -> Dict:

        self.creator_xp.setdefault(
            creator_id,
            0
        )

        self.creator_xp[creator_id] += xp

        level = self.calculate_level(
            self.creator_xp[creator_id]
        )

        self.creator_levels[
            creator_id
        ] = level

        reward = {
            "creator_id": creator_id,
            "xp_added": xp,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.reward_history.append(reward)

        self.check_badges(creator_id)

        return {
            "success": True,
            "xp": self.creator_xp[creator_id],
            "level": level
        }

    # ==================================================
    # CALCULATE LEVEL
    # ==================================================

    def calculate_level(
        self,
        xp: int
    ) -> int:

        return (xp // 100) + 1

    # ==================================================
    # BADGE CHECK
    # ==================================================

    def check_badges(
        self,
        creator_id: int
    ):

        xp = self.creator_xp.get(
            creator_id,
            0
        )

        self.creator_badges.setdefault(
            creator_id,
            []
        )

        for threshold, badge in self.BADGES.items():

            if (
                xp >= threshold and
                badge not in self.creator_badges[creator_id]
            ):

                self.creator_badges[
                    creator_id
                ].append(badge)

    # ==================================================
    # GET LEVEL
    # ==================================================

    def get_level(
        self,
        creator_id: int
    ) -> int:

        return self.creator_levels.get(
            creator_id,
            1
        )

    # ==================================================
    # GET XP
    # ==================================================

    def get_xp(
        self,
        creator_id: int
    ) -> int:

        return self.creator_xp.get(
            creator_id,
            0
        )

    # ==================================================
    # GET BADGES
    # ==================================================

    def get_badges(
        self,
        creator_id: int
    ) -> List[str]:

        return self.creator_badges.get(
            creator_id,
            []
        )

    # ==================================================
    # FOLLOWER MILESTONE
    # ==================================================

    def follower_milestone(
        self,
        creator_id: int,
        follower_count: int
    ) -> Dict:

        rewards = {
            100: 50,
            500: 100,
            1000: 250,
            5000: 500,
            10000: 1000,
            50000: 2500
        }

        if follower_count in rewards:

            return self.add_xp(
                creator_id,
                rewards[follower_count],
                f"{follower_count} followers"
            )

        return {
            "success": False
        }

    # ==================================================
    # POST ENGAGEMENT REWARD
    # ==================================================

    def engagement_reward(
        self,
        creator_id: int,
        likes: int,
        comments: int,
        shares: int
    ) -> Dict:

        xp = (
            likes * 1 +
            comments * 3 +
            shares * 5
        )

        return self.add_xp(
            creator_id,
            xp,
            "engagement"
        )

    # ==================================================
    # DAILY STREAK
    # ==================================================

    def streak_reward(
        self,
        creator_id: int,
        streak_days: int
    ) -> Dict:

        xp = streak_days * 10

        return self.add_xp(
            creator_id,
            xp,
            f"{streak_days} day streak"
        )

    # ==================================================
    # LEADERBOARD
    # ==================================================

    def leaderboard(
        self,
        limit: int = 50
    ):

        return sorted(
            self.creator_xp.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

    # ==================================================
    # PROFILE SUMMARY
    # ==================================================

    def creator_summary(
        self,
        creator_id: int
    ) -> Dict:

        return {
            "creator_id": creator_id,
            "xp": self.get_xp(creator_id),
            "level": self.get_level(creator_id),
            "badges": self.get_badges(creator_id)
        }


creator_rewards = CreatorRewards()