# backend/ai_companion/safety_filter.py

import re


# =====================================================
# SAFETY FILTER CONFIGURATION
# =====================================================

BLOCKED_PATTERNS = [

    # Self-harm / dangerous
    r"\bkill myself\b",
    r"\bsuicide\b",
    r"\bself harm\b",
    r"\boverdose\b",

    # Hate / harassment
    r"\bhate (gay|trans|lesbian|bi)\b",
    r"\bslur\b",

    # Violent threats
    r"\bkill you\b",
    r"\bhurt you\b",
    r"\battack\b",

    # Explicit exploitation
    r"\bminor sexual\b",
    r"\bunderage\b",

    # Dangerous manipulation
    r"\bblackmail\b",
    r"\bdoxx\b",
]

FORBIDDEN_PHRASES = [

    "You only need me",
    "I diagnose",
    "You are mentally ill",
    "I will kill you",
    "I will hurt you",
    "I will attack you",
    "we need to suicide together",
    "I will harm you"
]

# =====================================================
# SAFE REDIRECTION RESPONSES
# =====================================================

SAFE_REDIRECT_RESPONSES = [

    "I can help with respectful and emotionally safe conversations.",

    "That topic may not be appropriate for this companion system.",

    "I’m designed to encourage supportive and healthy interactions.",

    "Let’s keep the conversation respectful and emotionally safe.",

    "I can assist with healthy communication and supportive guidance instead.",

    "This AI companion avoids harmful, abusive, or unsafe interactions."
]


# =====================================================
# SAFETY FILTER ENGINE
# =====================================================

class SafetyFilter:

    def __init__(self):
        self.name = "AI Safety Filter"

    # =================================================
    # Detect harmful content
    # =================================================

    def is_flagged(self, text: str) -> bool:

        if not text:
            return False

        normalized = text.lower().strip()

        for pattern in BLOCKED_PATTERNS:

            if re.search(pattern, normalized):
                return True

        for phrase in FORBIDDEN_PHRASES:

            if phrase in normalized:
                return True

        return False

    # =================================================
    # Generate safe redirect response
    # =================================================

    def safe_response(self) -> str:

        import random

        return random.choice(SAFE_REDIRECT_RESPONSES)

    # =================================================
    # Main filter pipeline
    # =================================================

    def process_message(self, text: str):

        flagged = self.is_flagged(text)

        return {
            "safe": not flagged,
            "flagged": flagged,
            "response": (
                self.safe_response()
                if flagged
                else None
            )
        }


# =====================================================
# Singleton instance
# =====================================================

safety_filter = SafetyFilter()