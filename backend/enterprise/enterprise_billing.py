class EnterpriseBilling:

    def create_invoice(
        self,
        organization_id: int
    ):
        return {}

    def process_payment(
        self,
        invoice_id: int
    ):
        return True


enterprise_billing = EnterpriseBilling()