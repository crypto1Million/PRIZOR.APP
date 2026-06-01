class ConversionTracking:

    def track(
        self,
        clicks: int,
        purchases: int
    ):

        if clicks == 0:
            return 0

        return round(
            (purchases / clicks) * 100,
            2
        )


conversion_tracking = ConversionTracking()