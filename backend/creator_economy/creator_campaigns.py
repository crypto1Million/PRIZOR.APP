# backend/creator_economy/creator_campaigns.py

from datetime import datetime
from typing import Dict, List
import uuid


class CreatorCampaigns:
    """
    Creator Campaign Engine

    Supports:

    - Product launches
    - Merch drops
    - Event promotions
    - Sponsorship campaigns
    - Creator challenges
    - Conversion tracking
    - ROI analytics
    """

    def __init__(self):

        self.campaigns = {}
        self.conversions = {}
        self.clicks = {}
        self.impressions = {}

    # ==================================================
    # CREATE CAMPAIGN
    # ==================================================

    def create_campaign(
        self,
        creator_id: int,
        title: str,
        campaign_type: str,
        budget: float = 0.0
    ) -> Dict:

        campaign_id = str(uuid.uuid4())

        campaign = {
            "campaign_id": campaign_id,
            "creator_id": creator_id,
            "title": title,
            "campaign_type": campaign_type,
            "budget": budget,
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }

        self.campaigns[campaign_id] = campaign

        self.clicks[campaign_id] = 0
        self.impressions[campaign_id] = 0
        self.conversions[campaign_id] = 0

        return campaign

    # ==================================================
    # TRACK IMPRESSION
    # ==================================================

    def track_impression(
        self,
        campaign_id: str
    ):

        if campaign_id in self.impressions:
            self.impressions[campaign_id] += 1

    # ==================================================
    # TRACK CLICK
    # ==================================================

    def track_click(
        self,
        campaign_id: str
    ):

        if campaign_id in self.clicks:
            self.clicks[campaign_id] += 1

    # ==================================================
    # TRACK CONVERSION
    # ==================================================

    def track_conversion(
        self,
        campaign_id: str
    ):

        if campaign_id in self.conversions:
            self.conversions[campaign_id] += 1

    # ==================================================
    # CLICK THROUGH RATE
    # ==================================================

    def ctr(
        self,
        campaign_id: str
    ) -> float:

        impressions = self.impressions.get(
            campaign_id,
            0
        )

        if impressions == 0:
            return 0.0

        return round(
            (
                self.clicks[campaign_id]
                /
                impressions
            ) * 100,
            2
        )

    # ==================================================
    # CONVERSION RATE
    # ==================================================

    def conversion_rate(
        self,
        campaign_id: str
    ) -> float:

        clicks = self.clicks.get(
            campaign_id,
            0
        )

        if clicks == 0:
            return 0.0

        return round(
            (
                self.conversions[campaign_id]
                /
                clicks
            ) * 100,
            2
        )

    # ==================================================
    # ROI
    # ==================================================

    def roi(
        self,
        campaign_id: str,
        revenue_generated: float
    ) -> float:

        budget = self.campaigns[
            campaign_id
        ]["budget"]

        if budget == 0:
            return revenue_generated

        return round(
            (
                (
                    revenue_generated
                    -
                    budget
                )
                /
                budget
            )
            * 100,
            2
        )

    # ==================================================
    # CAMPAIGN ANALYTICS
    # ==================================================

    def analytics(
        self,
        campaign_id: str
    ) -> Dict:

        return {
            "campaign_id":
                campaign_id,

            "impressions":
                self.impressions.get(
                    campaign_id,
                    0
                ),

            "clicks":
                self.clicks.get(
                    campaign_id,
                    0
                ),

            "conversions":
                self.conversions.get(
                    campaign_id,
                    0
                ),

            "ctr":
                self.ctr(
                    campaign_id
                ),

            "conversion_rate":
                self.conversion_rate(
                    campaign_id
                )
        }

    # ==================================================
    # GET CAMPAIGNS
    # ==================================================

    def creator_campaigns(
        self,
        creator_id: int
    ) -> List[Dict]:

        return [
            campaign
            for campaign
            in self.campaigns.values()
            if campaign["creator_id"]
            == creator_id
        ]

    # ==================================================
    # END CAMPAIGN
    # ==================================================

    def end_campaign(
        self,
        campaign_id: str
    ) -> Dict:

        if campaign_id not in self.campaigns:

            return {
                "success": False
            }

        self.campaigns[
            campaign_id
        ]["status"] = "ended"

        return {
            "success": True
        }

    # ==================================================
    # TRENDING CAMPAIGNS
    # ==================================================

    def trending_campaigns(
        self,
        limit: int = 20
    ):

        campaigns = []

        for campaign_id in self.campaigns:

            score = (
                self.impressions.get(
                    campaign_id,
                    0
                )
                +
                self.clicks.get(
                    campaign_id,
                    0
                ) * 5
                +
                self.conversions.get(
                    campaign_id,
                    0
                ) * 20
            )

            campaigns.append(
                (
                    campaign_id,
                    score
                )
            )

        return sorted(
            campaigns,
            key=lambda x: x[1],
            reverse=True
        )[:limit]


creator_campaigns = CreatorCampaigns()