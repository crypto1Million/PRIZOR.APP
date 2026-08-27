from __future__ import annotations

from backend.matching_engine.distance_service import (
    DistanceService,
)


class DistanceFilter:
    """
    Removes candidates outside the user's
    configured maximum dating distance.
    """

    @classmethod
    def matches(
        cls,
        user_latitude: float | None,
        user_longitude: float | None,
        candidate_latitude: float | None,
        candidate_longitude: float | None,
        max_distance_km: float,
    ) -> bool:

        if max_distance_km < 0:
            raise ValueError(
                "max_distance_km cannot be negative"
            )

        if None in (
            user_latitude,
            user_longitude,
            candidate_latitude,
            candidate_longitude,
        ):
            return False

        distance = DistanceService.calculate(
            user_latitude,
            user_longitude,
            candidate_latitude,
            candidate_longitude,
        )

        return distance <= max_distance_km

    @classmethod
    def filter(
        cls,
        candidates,
        user_latitude: float,
        user_longitude: float,
        max_distance_km: float,
    ):
        result = []

        for candidate in candidates:

            candidate_latitude = getattr(
                candidate,
                "latitude",
                None,
            )

            candidate_longitude = getattr(
                candidate,
                "longitude",
                None,
            )

            if cls.matches(
                user_latitude,
                user_longitude,
                candidate_latitude,
                candidate_longitude,
                max_distance_km,
            ):
                result.append(candidate)

        return result