class AgencyBrandDeals:

    def create_deal(
        self,
        agency_id: int,
        brand_id: int
    ):

        return {
            "agency_id": agency_id,
            "brand_id": brand_id
        }

    def approve_deal(
        self,
        deal_id: int
    ):

        return True


agency_brand_deals = AgencyBrandDeals()