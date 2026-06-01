class BrandProfiles:

    def build_profile(
        self,
        brand_name: str,
        category: str
    ):

        return {
            "brand_name": brand_name,
            "category": category,
            "status": "active"
        }


brand_profiles = BrandProfiles()