# backend/ai_companion/connection_support.py

import random
from backend.ai_companion.connection_support import connection_support


# =====================================================
# CONNECTION & DISAPPOINTMENT SUPPORT RESPONSES
# =====================================================

CONNECTION_SUPPORT_RESPONSES = [

    "Not every connection develops the way we hope, and that’s okay.",

    "Someone losing interest does not reduce your value.",

    "Compatibility is mutual — it cannot be forced.",

    "Some conversations naturally fade, and that is part of social life.",

    "A difficult interaction does not define your future connections.",

    "The healthiest connections usually feel balanced and natural.",

    "You deserve conversations where interest and effort feel mutual.",

    "It’s okay to step away from interactions that feel emotionally draining.",

    "Not every person will understand your energy, and that’s normal.",

    "Sometimes the right connection simply arrives at a different time."
]


# =====================================================
# ENCOURAGEMENT RESPONSES
# =====================================================

ENCOURAGEMENT_RESPONSES = [

    "Your authenticity matters more than trying to impress everyone.",

    "You are allowed to move at a pace that feels comfortable.",

    "Confidence often grows through honest self-expression.",

    "Healthy communication should never feel forced or pressured.",

    "You deserve respectful and emotionally safe conversations.",

    "Being yourself creates stronger long-term compatibility.",

    "Good connections usually develop through comfort and trust.",

    "You do not need universal approval to have meaningful relationships."
]


# =====================================================
# CONNECTION SUPPORT ENGINE
# =====================================================

class ConnectionSupport:

    def __init__(self):
        self.name = "Connection Support Engine"

    # =================================================
    # Main support generator
    # =================================================

    def generate_response(
        self,
        support_type: str = "connection"
    ) -> str:

        if support_type == "encouragement":
            return self._encouragement_response()

        return self._connection_response()

    # =================================================
    # Internal response selectors
    # =================================================

    def _connection_response(self) -> str:
        return random.choice(CONNECTION_SUPPORT_RESPONSES)

    def _encouragement_response(self) -> str:
        return random.choice(ENCOURAGEMENT_RESPONSES)


# =====================================================
# Singleton instance
# =====================================================

connection_support = ConnectionSupport()