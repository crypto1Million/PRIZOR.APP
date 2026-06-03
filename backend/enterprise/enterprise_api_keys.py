import secrets


class EnterpriseAPIKeys:

    def generate_key(self):

        return secrets.token_hex(32)


enterprise_api_keys = EnterpriseAPIKeys()