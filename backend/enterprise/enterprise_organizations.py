class EnterpriseOrganizations:

    def create_organization(
        self,
        name: str
    ):
        return {
            "name": name
        }

    def get_organization(
        self,
        organization_id: int
    ):
        return {}


enterprise_organizations = EnterpriseOrganizations()