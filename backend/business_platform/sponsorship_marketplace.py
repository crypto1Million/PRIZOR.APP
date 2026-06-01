class SponsorshipMarketplace:

    def create_listing(
        self,
        brand_id: int,
        title: str,
        budget: float
    ):

        return {
            "brand_id": brand_id,
            "title": title,
            "budget": budget
        }


sponsorship_marketplace = SponsorshipMarketplace()