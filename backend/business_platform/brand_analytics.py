class BrandAnalytics:

    def overview(
        self,
        impressions: int,
        clicks: int,
        conversions: int
    ):

        ctr = 0

        if impressions > 0:
            ctr = (clicks / impressions) * 100

        return {
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "ctr": round(ctr, 2)
        }


brand_analytics = BrandAnalytics()