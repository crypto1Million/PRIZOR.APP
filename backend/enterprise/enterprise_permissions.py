class EnterprisePermissions:

    def grant_permission(
        self,
        role_id: int,
        permission: str
    ):
        return True

    def revoke_permission(
        self,
        role_id: int,
        permission: str
    ):
        return True


enterprise_permissions = EnterprisePermissions()