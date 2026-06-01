class BrandVerification:

    def verify(
        self,
        website_verified: bool,
        business_document_verified: bool
    ):

        if website_verified and business_document_verified:
            return {
                "verified": True,
                "level": "gold"
            }

        return {
            "verified": False,
            "level": "pending"
        }


brand_verification = BrandVerification()