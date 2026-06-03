class EnterpriseSecurity:

    def enable_mfa(
        self,
        organization_id: int
    ):
        return True

    def enforce_security_policy(
        self,
        organization_id: int
    ):
        return True


enterprise_security = EnterpriseSecurity()