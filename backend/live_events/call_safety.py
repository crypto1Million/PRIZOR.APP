class CallSafety:

    banned_keywords = [
        "threat",
        "violence",
        "harassment"
    ]

    def check_message(
        self,
        text: str
    ):

        text = text.lower()

        for keyword in self.banned_keywords:

            if keyword in text:
                return {
                    "safe": False,
                    "reason": keyword
                }

        return {
            "safe": True
        }


call_safety = CallSafety()