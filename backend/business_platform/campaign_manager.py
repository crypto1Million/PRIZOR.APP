class CampaignManager:

    def launch_campaign(
        self,
        campaign_name: str
    ):

        return {
            "campaign": campaign_name,
            "status": "active"
        }


campaign_manager = CampaignManager()