class AgencyRoster:

    def add_creator(
        self,
        agency_id: int,
        creator_id: int
    ):

        return True

    def remove_creator(
        self,
        agency_id: int,
        creator_id: int
    ):

        return True

    def get_roster(
        self,
        agency_id: int
    ):

        return []


agency_roster = AgencyRoster()