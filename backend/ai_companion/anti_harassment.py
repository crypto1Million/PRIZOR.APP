# backend/ai_companion/anti_harassment.py

import random


# =====================================================
# ANTI-HARASSMENT SUPPORT RESPONSES
# =====================================================

ANTI_HARASSMENT_RESPONSES = [

    "You are allowed to disengage from disrespectful interactions.",

    "Blocking harmful users is sometimes the healthiest decision.",

    "Nobody is entitled to your emotional energy or attention.",

    "Mutual respect should always be the minimum standard.",

    "You do not need to tolerate manipulation or intimidation.",

    "Protecting your emotional safety is important.",

    "It’s okay to leave conversations that feel hostile or unsafe.",

    "Healthy communities are built on respect and consent.",

    "You deserve interactions that feel emotionally safe.",

    "Disrespectful behavior is a reflection of them, not your worth."
]


# =====================================================
# BOUNDARY SUPPORT RESPONSES
# =====================================================

BOUNDARY_SUPPORT_RESPONSES = [

    "Setting boundaries is healthy, not rude.",

    "You are allowed to say no without explaining everything.",

    "Respectful people will understand clear boundaries.",

    "Your comfort matters during every interaction.",

    "Healthy communication includes respecting personal limits.",

    "You do not owe constant availability to anyone.",

    "Protecting your peace is completely valid.",

    "Boundaries help create safer and healthier conversations."
]


# =====================================================
# COMMUNITY SAFETY RESPONSES
# =====================================================

COMMUNITY_SAFETY_RESPONSES = [

    "Supportive communities prioritize respect and inclusion.",

    "Harassment should never be normalized in social spaces.",

    "Safe spaces are built through empathy and accountability.",

    "Everyone deserves respectful treatment regardless of identity.",

    "Healthy communities encourage kindness and emotional safety.",

    "You are allowed to report harmful or abusive behavior."
]


# =====================================================
# ANTI-HARASSMENT ENGINE
# =====================================================

class AntiHarassment:

    def __init__(self):
        self.name = "Anti Harassment Engine"

    # =================================================
    # Main response generator
    # =================================================

    def generate_response(
        self,
        response_type: str = "general"
    ) -> str:

        if response_type == "boundaries":
            return self._boundary_response()

        elif response_type == "community":
            return self._community_response()

        return self._anti_harassment_response()

    # =================================================
    # Internal selectors
    # =================================================

    def _anti_harassment_response(self) -> str:
        return random.choice(ANTI_HARASSMENT_RESPONSES)

    def _boundary_response(self) -> str:
        return random.choice(BOUNDARY_SUPPORT_RESPONSES)

    def _community_response(self) -> str:
        return random.choice(COMMUNITY_SAFETY_RESPONSES)


# =====================================================
# Singleton instance
# =====================================================

anti_harassment = AntiHarassment()