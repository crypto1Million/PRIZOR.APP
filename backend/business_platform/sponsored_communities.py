class SponsoredCommunities:

    def sponsor(
        self,
        community_id: int,
        brand_id: int
    ):

        return {
            "community_id": community_id,
            "brand_id": brand_id,
            "status": "sponsored"
        }


sponsored_communities = SponsoredCommunities()