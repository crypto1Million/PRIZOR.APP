class AgencyCommissions:

    def calculate_commission(
        self,
        revenue: float,
        percentage: float
    ):

        return revenue * percentage / 100


agency_commissions = AgencyCommissions()