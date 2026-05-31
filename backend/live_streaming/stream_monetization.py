class StreamMonetization:

    PLATFORM_FEE = 0.10

    def creator_earnings(
        self,
        gross_amount: float
    ):

        fee = gross_amount * self.PLATFORM_FEE

        return {
            "gross": gross_amount,
            "platform_fee": fee,
            "creator_amount": gross_amount - fee
        }


stream_monetization = StreamMonetization()