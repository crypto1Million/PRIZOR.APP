class BusinessRevenue:

    def calculate(
        self,
        sponsorship_revenue: float,
        ad_revenue: float,
        commerce_revenue: float
    ):

        total = (
            sponsorship_revenue +
            ad_revenue +
            commerce_revenue
        )

        return {
            "total_revenue": total
        }


business_revenue = BusinessRevenue()