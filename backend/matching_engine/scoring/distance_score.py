from __future__ import annotations

from math import exp


class DistanceScore:
    """
    Converts geographic distance into a 0-100 score.

    Distance is measured in kilometers.
    """

    @staticmethod
    def calculate(
        distance_km: float | None,
        decay_km: float = 50.0,
    ) -> float:

        if distance_km is None:
            return 0.0

        if distance_km < 0:
            raise ValueError(
                "distance_km cannot be negative"
            )

        if decay_km <= 0:
            raise ValueError(
                "decay_km must be greater than zero"
            )

        score = 100.0 * exp(
            -distance_km / decay_km
        )

        return round(
            max(0.0, min(100.0, score)),
            4,
        )