class AgencyPermissions:

    def assign_role(
        self,
        member_id: int,
        role: str
    ):

        return True

    def check_permission(
        self,
        member_id: int,
        permission: str
    ):

        return True


agency_permissions = AgencyPermissions()