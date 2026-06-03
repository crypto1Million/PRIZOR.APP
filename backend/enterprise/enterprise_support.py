class EnterpriseSupport:

    def create_ticket(
        self,
        organization_id: int
    ):
        return {}

    def assign_priority(
        self,
        ticket_id: int
    ):
        return True


enterprise_support = EnterpriseSupport()