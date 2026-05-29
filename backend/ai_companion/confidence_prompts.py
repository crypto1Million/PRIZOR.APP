# backend/ai_companion/confidence_prompts.py

import random


# =====================================================
# SELF-CONFIDENCE PROMPTS
# =====================================================

CONFIDENCE_PROMPTS = [

    "Authenticity usually creates stronger connections.",

    "You do not need to impress everyone to be valued.",

    "Confidence grows when you stop chasing constant approval.",

    "Your comfort matters just as much as theirs.",

    "Healthy conversations should feel natural, not performative.",

    "You are allowed to take up space without apologizing.",

    "Being genuine often attracts more meaningful people.",

    "You do not need to change yourself for basic respect.",

    "Real compatibility is built through mutual understanding.",

    "You deserve interactions that feel emotionally safe.",

    "Not every conversation needs to become something serious.",

    "It’s okay to move at a pace that feels comfortable.",

    "Your value is not determined by attention from others.",

    "Strong boundaries can protect emotional energy.",

    "Good connections usually grow through honesty and trust."
]


# =====================================================
# SOCIAL CONFIDENCE PROMPTS
# =====================================================

SOCIAL_CONFIDENCE_PROMPTS = [

    "Curiosity creates better conversations than pressure.",

    "Listening carefully can build stronger emotional connection.",

    "You do not need perfect words to have meaningful conversations.",

    "Confidence often comes from comfort, not performance.",

    "Respectful communication is more attractive than forced confidence.",

    "Healthy interactions usually involve balanced effort.",

    "You are allowed to pause before responding.",

    "People often connect more deeply with honesty than perfection."
]


# =====================================================
# DAILY ENCOURAGEMENT PROMPTS
# =====================================================

DAILY_ENCOURAGEMENT_PROMPTS = [

    "A single interaction does not define your worth.",

    "Some of the best connections happen naturally over time.",

    "You deserve patience, respect, and emotional safety.",

    "It’s completely okay to protect your peace.",

    "Not everyone will understand you, and that is normal.",

    "Your identity and boundaries deserve respect.",

    "Taking things slowly can create healthier experiences.",

    "You are allowed to prioritize emotional comfort."
]


# =====================================================
# CONFIDENCE PROMPT ENGINE
# =====================================================

class ConfidencePrompts:

    def __init__(self):
        self.name = "Confidence Prompt Engine"

    # =================================================
    # Main prompt selector
    # =================================================

    def generate_prompt(
        self,
        prompt_type: str = "confidence"
    ) -> str:

        if prompt_type == "social":
            return self._social_prompt()

        elif prompt_type == "daily":
            return self._daily_prompt()

        return self._confidence_prompt()

    def generate_confidence_prompt(self):

        prompts = [

            "You deserve connections where you feel respected and valued.",

            "Confidence grows when you stop shrinking yourself for others.",

            "Your identity is valid and worthy of healthy relationships.",

            "Healthy relationships begin with authenticity.",

            "You do not need to become someone else to be appreciated."

        ]

        return random.choice(prompts)

    # =================================================
    # Internal generators
    # =================================================

    def _confidence_prompt(self) -> str:
        return random.choice(CONFIDENCE_PROMPTS)

    def _social_prompt(self) -> str:
        return random.choice(SOCIAL_CONFIDENCE_PROMPTS)

    def _daily_prompt(self) -> str:
        return random.choice(DAILY_ENCOURAGEMENT_PROMPTS)


# =====================================================
# Singleton instance
# =====================================================

confidence_prompts = ConfidencePrompts()