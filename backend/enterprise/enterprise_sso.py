class EnterpriseSSO:

    def enable_saml(self):
        return True

    def enable_oidc(self):
        return True


enterprise_sso = EnterpriseSSO()