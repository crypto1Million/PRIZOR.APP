class AdEngine:

    def create_ad(
        self,
        title: str,
        destination_url: str
    ):

        return {
            "title": title,
            "destination": destination_url,
            "status": "approved"
        }


ad_engine = AdEngine()