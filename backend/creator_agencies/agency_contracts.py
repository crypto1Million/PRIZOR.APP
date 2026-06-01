class AgencyContracts:

    def create_contract(
        self,
        creator_id: int,
        agency_id: int
    ):

        return {
            "creator_id": creator_id,
            "agency_id": agency_id,
            "status": "pending"
        }

    def approve_contract(
        self,
        contract_id: int
    ):

        return True


agency_contracts = AgencyContracts()