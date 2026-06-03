class EnterpriseDashboard:

    def dashboard(
        self,
        organization_id: int
    ):
        return {
            "organizations": 0,
            "users": 0,
            "revenue": 0
        }


enterprise_dashboard = EnterpriseDashboard()