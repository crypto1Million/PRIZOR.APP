# backend/ai_companion/companion_engine.py

from backend.ai_companion.response_router import route_response
from backend.ai_companion.safety_filter import filter_response
from backend.ai_companion.connection_support import connection_support


class CompanionEngine:
    """
    Main AI Companion orchestration engine.

    Responsibilities:
    - Receive user message
    - Build emotional context
    - Route to correct emotional module
    - Apply safety filtering
    - Return final AI response
    """

    def __init__(self):
        self.name = "Prizor Companion"

    def generate_response(
        self,
        user_id: int,
        message: str,
        memory: dict | None = None
    ) -> dict:
        """
        Generate emotionally intelligent companion response.
        """

        # -----------------------------
        # Step 1: Normalize input
        # -----------------------------
        clean_message = message.strip()

        # -----------------------------
        # Step 2: Build emotional context
        # -----------------------------
        emotional_context = self._build_context(
            message=clean_message,
            memory=memory
        )

        # -----------------------------
        # Step 3: Route response
        # -----------------------------
        raw_response = route_response(
            message=clean_message,
            context=emotional_context
        )

        # -----------------------------
        # Step 4: Apply safety filters
        # -----------------------------
        safe_response = filter_response(raw_response)

        # -----------------------------
        # Step 5: Return structured output
        # -----------------------------
        return {
            "success": True,
            "response": safe_response,
            "emotion_detected": emotional_context["emotion"],
            "support_mode": emotional_context["support_mode"]
        }

    def _build_context(
        self,
        message: str,
        memory: dict | None = None
    ) -> dict:
        """
        Detect emotional context from message.
        """

        lowered = message.lower()

        emotion = "neutral"
        support_mode = "general"

        # -----------------------------
        # Rejection detection
        # -----------------------------
        rejection_keywords = [
            "ghosted",
            "ignored",
            "rejected",
            "unmatched",
            "left me",
            "blocked"
        ]

        # -----------------------------
        # Anxiety / stress indicators
        # -----------------------------
        stress_keywords = [
            "anxious",
            "nervous",
            "scared",
            "worried",
            "stress"
        ]

        # -----------------------------
        # Harassment indicators
        # -----------------------------
        harassment_keywords = [
            "harassed",
            "abused",
            "threatened",
            "bullied",
            "hate"
        ]

        # -----------------------------
        # Emotion classification
        # -----------------------------
        if any(word in lowered for word in rejection_keywords):
            emotion = "rejection"
            support_mode = "emotional_support"

        elif any(word in lowered for word in stress_keywords):
            emotion = "stress"
            support_mode = "confidence_support"

        elif any(word in lowered for word in harassment_keywords):
            emotion = "harassment"
            support_mode = "safety_support"

        # -----------------------------
        # User preference memory
        # -----------------------------
        communication_style = "balanced"

        if memory:
            communication_style = memory.get(
                "communication_style",
                "balanced"
            )

        return {
            "emotion": emotion,
            "support_mode": support_mode,
            "communication_style": communication_style
        }


# ---------------------------------------------------
# Singleton engine instance
# ---------------------------------------------------

companion_engine = CompanionEngine()