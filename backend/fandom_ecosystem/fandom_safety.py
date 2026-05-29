# backend/fandom_ecosystem/fandom_safety.py

class FandomSafety:

    BLOCKED_TERMS = [

        "hate",
        "slur",
        "harassment",
        "threat"
    ]

    def validate_message(self, text: str):

        lowered = text.lower()

        for word in self.BLOCKED_TERMS:

            if word in lowered:

                return {
                    "safe": False,
                    "reason": f"Detected unsafe term: {word}"
                }

        return {
            "safe": True
        }