from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PreferenceInput:
    age_match: float = 0.0
    gender_match: float = 0.0
    relationship_goal_match: float = 0.0
    lifestyle_match: float = 0.0


class PreferenceScore:
    """
    Calculates preference compatibility.

    Every input is expected to be 0-100.
    """

    WEIGHTS = {
        "age_match": 0.20,
        "gender_match": 0.30,
        "relationship_goal_match": 0.30,
        "lifestyle_match": 0.20,
    }

    @classmethod
    def calculate(
        cls,
        preferences: PreferenceInput,
    ) -> float:

        values = {
            "age_match": preferences.age_match,
            "gender_match": preferences.gender_match,
            "relationship_goal_match":
                preferences.relationship_goal_match,
            "lifestyle_match":
                preferences.lifestyle_match,
        }

        score = sum(
            max(0.0, min(100.0, value))
            * cls.WEIGHTS[name]
            for name, value in values.items()
        )

        return round(score, 4)