class PurchasePrediction:

    def predict_purchase(
        self,
        user_id: int,
        product_id: int
    ):
        return {
            "purchase_probability": 0.0
        }

    def lifetime_value(
        self,
        user_id: int
    ):
        return {
            "ltv": 0
        }


purchase_prediction = PurchasePrediction()