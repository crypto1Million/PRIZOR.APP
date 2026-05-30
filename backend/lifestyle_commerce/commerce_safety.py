# backend/lifestyle_commerce/commerce_safety.py

class CommerceSafety:

    BLOCKED_KEYWORDS = [
        "scam",
        "fraud",
        "counterfeit"
    ]

    def is_allowed(self, text: str):

        text = text.lower()

        return not any(
            word in text
            for word in self.BLOCKED_KEYWORDS
        )


commerce_safety = CommerceSafety()