from math import radians, sin, cos, sqrt, atan2


class DistanceService:

    EARTH_RADIUS_KM = 6371.0

    @classmethod
    def calculate(
        cls,
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float,
    ) -> float:

        lat1 = radians(lat1)
        lat2 = radians(lat2)

        dlat = lat2 - lat1
        dlon = radians(lon2 - lon1)

        a = (
            sin(dlat / 2) ** 2
            + cos(lat1)
            * cos(lat2)
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a),
        )

        return cls.EARTH_RADIUS_KM * c