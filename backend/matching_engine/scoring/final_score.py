from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoreComponents:
    compatibility: float
    distance: float
    interest: float
    activity: float
    preference: float


class FinalScore:
    """
    Combines all matching signals into a final score.

    Output range: 0-100.
    """

    WEIGHTS = {
        "compatibility": 0.30,
        "distance": 0.10,
        "interest": 0.20,
        "activity": 0.10,
        "preference": 0.30,
    }

    @classmethod
    def calculate(
        cls,
        components: ScoreComponents,
    ) -> float:

        values = {
            "compatibility":
                components.compatibility,

            "distance":
                components.distance,

            "interest":
                components.interest,

            "activity":
                components.activity,

            "preference":
                components.preference,
        }

        score = sum(
            max(0.0, min(100.0, value))
            * cls.WEIGHTS[name]
            for name, value in values.items()
        )

        return round(
            max(0.0, min(100.0, score)),
            4,
        )