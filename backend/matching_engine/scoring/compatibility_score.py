from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompatibilityFeatures:
    personality: float = 0.0
    lifestyle: float = 0.0
    values: float = 0.0
    communication: float = 0.0
    relationship_goals: float = 0.0


class CompatibilityScore:
    """
    Calculates compatibility between two users.

    Every feature is expected to be in the range 0-100.
    Returns a normalized score in the range 0-100.
    """

    WEIGHTS = {
        "personality": 0.25,
        "lifestyle": 0.20,
        "values": 0.20,
        "communication": 0.15,
        "relationship_goals": 0.20,
    }

    @classmethod
    def calculate(
        cls,
        features: CompatibilityFeatures,
    ) -> float:

        values = {
            "personality": features.personality,
            "lifestyle": features.lifestyle,
            "values": features.values,
            "communication": features.communication,
            "relationship_goals": features.relationship_goals,
        }

        score = sum(
            max(0.0, min(100.0, value))
            * cls.WEIGHTS[name]
            for name, value in values.items()
        )

        return round(score, 4)