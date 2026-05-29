# backend/ai_companion/healthy_communication.py

import random


# =====================================================
# HEALTHY COMMUNICATION RESPONSES
# =====================================================

HEALTHY_COMMUNICATION_RESPONSES = [

    "Clear communication usually prevents unnecessary confusion.",

    "Healthy conversations involve mutual respect and effort.",

    "You are allowed to express boundaries respectfully.",

    "Good communication should feel safe, not pressured.",

    "Listening carefully can strengthen emotional connection.",

    "Honest conversations are usually healthier than performative ones.",

    "Mutual understanding grows through patience and respect.",

    "You do not need to tolerate disrespect to maintain a conversation.",

    "Healthy interactions often involve balanced emotional energy.",

    "Kindness and clarity usually create better outcomes."
]


# =====================================================
# SAFER CONVERSATION PROMPTS
# =====================================================

SAFER_CONVERSATION_PROMPTS = [

    "Take time before sharing deeply personal information online.",

    "Trust should develop gradually through consistent behavior.",

    "You are allowed to leave conversations that feel uncomfortable.",

    "Healthy boundaries are an important part of emotional safety.",

    "Respectful communication should always remain mutual.",

    "If something feels unsafe or manipulative, it’s okay to disengage.",

    "Protecting emotional comfort is a valid priority.",

    "Not every conversation deserves continued emotional investment."
]


# =====================================================
# CONFLICT DE-ESCALATION RESPONSES
# =====================================================

DE_ESCALATION_RESPONSES = [

    "Slowing down a heated conversation can prevent misunderstandings.",

    "Respectful disagreement is healthier than personal attacks.",

    "Pausing before reacting can reduce emotional escalation.",

    "Clear and calm communication often improves difficult situations.",

    "It’s okay to step away from emotionally aggressive conversations.",

    "Healthy communication should not involve intimidation or pressure."
]


# =====================================================
# HEALTHY COMMUNICATION ENGINE
# =====================================================

class HealthyCommunication:

    def __init__(self):
        self.name = "Healthy Communication Engine"

    # =================================================
    # Main response generator
    # =================================================

    def generate_response(
        self,
        communication_type: str = "general"
    ) -> str:

        if communication_type == "safer":
            return self._safer_conversation_response()

        elif communication_type == "de_escalation":
            return self._de_escalation_response()

        return self._healthy_response()

    # =================================================
    # Internal response selectors
    # =================================================

    def _healthy_response(self) -> str:
        return random.choice(HEALTHY_COMMUNICATION_RESPONSES)

    def _safer_conversation_response(self) -> str:
        return random.choice(SAFER_CONVERSATION_PROMPTS)

    def _de_escalation_response(self) -> str:
        return random.choice(DE_ESCALATION_RESPONSES)


# =====================================================
# Singleton instance
# =====================================================

healthy_communication = HealthyCommunication()