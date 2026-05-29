# backend/ai_companion/response_router.py

from backend.ai_companion.safety_filter import safety_filter

from backend.ai_companion.emotional_guidance import (
    emotional_guidance
)

from backend.ai_companion.rejection_support import (
    rejection_support
)

from backend.ai_companion.confidence_prompts import (
    confidence_prompts
)

from backend.ai_companion.healthy_communication import (
    healthy_communication
)

from backend.ai_companion.anti_harassment import (
    anti_harassment
)


# =====================================================
# RESPONSE ROUTER
# =====================================================

class ResponseRouter:

    def __init__(self):

        self.name = "AI Companion Response Router"

    # =================================================
    # Main routing engine
    # =================================================

    def generate_response(self, user_message: str):

        # =============================================
        # SAFETY FILTER
        # =============================================

        safety_result = safety_filter.process_message(
            user_message
        )

        if safety_result["flagged"]:

            return {
                "type": "safety",
                "response": safety_result["response"]
            }

        # =============================================
        # NORMALIZED MESSAGE
        # =============================================

        text = user_message.lower()

        # =============================================
        # REJECTION SUPPORT
        # =============================================

        rejection_keywords = [
            "rejected",
            "ignored",
            "ghosted",
            "heartbroken",
            "blocked",
            "unmatched"
        ]

        if any(word in text for word in rejection_keywords):

            return {
                "type": "rejection_support",
                "response": (
                    rejection_support.generate_response()
                )
            }

        # =============================================
        # CONFIDENCE SUPPORT
        # =============================================

        confidence_keywords = [
            "insecure",
            "confidence",
            "nervous",
            "anxious",
            "scared",
            "shy"
        ]

        if any(word in text for word in confidence_keywords):

            return {
                "type": "confidence",
                "response": (
                    confidence_prompts.generate_prompt()
                )
            }

        # =============================================
        # HARASSMENT / BOUNDARIES
        # =============================================

        harassment_keywords = [
            "harassed",
            "bullied",
            "threatened",
            "unsafe",
            "abusive",
            "creepy"
        ]

        if any(word in text for word in harassment_keywords):

            return {
                "type": "anti_harassment",
                "response": (
                    anti_harassment.generate_response()
                )
            }

        # =============================================
        # HEALTHY COMMUNICATION
        # =============================================

        communication_keywords = [
            "argument",
            "communication",
            "conflict",
            "misunderstanding",
            "conversation",
            "boundary"
        ]

        if any(word in text for word in communication_keywords):

            return {
                "type": "healthy_communication",
                "response": (
                    healthy_communication.generate_response()
                )
            }

        # =============================================
        # DEFAULT EMOTIONAL GUIDANCE
        # =============================================

        return {
            "type": "emotional_guidance",
            "response": (
                emotional_guidance.generate_response()
            )
        }


# =====================================================
# SINGLETON INSTANCE
# =====================================================

response_router = ResponseRouter()