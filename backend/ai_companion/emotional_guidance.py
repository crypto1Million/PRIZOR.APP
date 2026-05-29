# backend/ai_companion/emotional_guidance.py

import random


# =====================================================
# SUPPORTIVE RESPONSE CATEGORIES
# =====================================================

REJECTION_SUPPORT = [
    "Not every connection reflects your value.",
    "Sometimes compatibility simply doesn't align naturally.",
    "Being rejected does not reduce your worth.",
    "The right conversations usually feel mutual, not forced.",
    "Someone losing interest is not proof that you are unworthy."
]

CONFIDENCE_SUPPORT = [
    "Authenticity usually creates stronger connections.",
    "You do not need to impress everyone to deserve attention.",
    "Confidence grows when you stop performing for approval.",
    "Your comfort matters too during conversations.",
    "You are allowed to move at your own pace."
]

HARASSMENT_SUPPORT = [
    "You are allowed to disengage from disrespectful conversations.",
    "Blocking harmful people is sometimes the healthiest choice.",
    "You do not owe anyone continued access to your attention.",
    "Protecting your emotional safety is important.",
    "Mutual respect should always be the baseline."
]

COMMUNICATION_SUPPORT = [
    "Clear communication often prevents misunderstandings.",
    "Healthy conversations usually involve balanced effort.",
    "Respectful curiosity creates better interactions.",
    "Setting boundaries early can reduce stress later.",
    "Good communication should feel safe, not pressured."
]

GENERAL_SUPPORT = [
    "You deserve conversations that feel comfortable and respectful.",
    "Not every interaction needs to become something serious.",
    "Taking things slowly is completely okay.",
    "Healthy connections usually develop naturally over time.",
    "Your boundaries and comfort matter."
]


# =====================================================
# MAIN EMOTIONAL GUIDANCE ENGINE
# =====================================================

class EmotionalGuidance:
    """
    Emotional guidance layer for Prizor AI Companion.

    IMPORTANT:
    - Non-medical
    - Non-therapeutic
    - Supportive only
    """

    def __init__(self):
        self.name = "Emotional Guidance Engine"

    # =================================================
    # Main dispatcher
    # =================================================

    def generate_support(
        self,
        emotion: str,
        communication_style: str = "balanced"
    ) -> str:

        if emotion == "rejection":
            return self._rejection_response()

        elif emotion == "stress":
            return self._confidence_response()

        elif emotion == "harassment":
            return self._harassment_response()

        elif emotion == "communication":
            return self._communication_response()

        return self._general_response()

    # =================================================
    # Response generators
    # =================================================

    def _rejection_response(self) -> str:
        return random.choice(REJECTION_SUPPORT)

    def _confidence_response(self) -> str:
        return random.choice(CONFIDENCE_SUPPORT)

    def _harassment_response(self) -> str:
        return random.choice(HARASSMENT_SUPPORT)

    def _communication_response(self) -> str:
        return random.choice(COMMUNICATION_SUPPORT)

    def _general_response(self) -> str:
        return random.choice(GENERAL_SUPPORT)


# =====================================================
# Singleton instance
# =====================================================

emotional_guidance = EmotionalGuidance()