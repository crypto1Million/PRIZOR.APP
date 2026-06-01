class CreatorPartnerships:

    def create_partnership(
        self,
        brand_id: int,
        creator_id: int
    ):

        return {
            "brand_id": brand_id,
            "creator_id": creator_id,
            "status": "pending"
        }


creator_partnerships = CreatorPartnerships()