class AgencyPayouts:

    def distribute_revenue(
        self,
        creator_id: int,
        amount: float
    ):

        return {
            "creator_id": creator_id,
            "amount": amount
        }


agency_payouts = AgencyPayouts()