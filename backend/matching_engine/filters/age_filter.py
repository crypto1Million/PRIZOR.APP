from __future__ import annotations


class AgeFilter:
    """
    Filters candidates according to the user's
    preferred age range.
    """

    @staticmethod
    def matches(
        candidate_age: int | None,
        min_age: int,
        max_age: int,
    ) -> bool:

        if candidate_age is None:
            return False

        if min_age > max_age:
            raise ValueError(
                "min_age cannot be greater than max_age"
            )

        if candidate_age < 18:
            return False

        return min_age <= candidate_age <= max_age

    @classmethod
    def filter(
        cls,
        candidates,
        min_age: int,
        max_age: int,
    ):
        return [
            candidate
            for candidate in candidates
            if cls.matches(
                getattr(candidate, "age", None),
                min_age,
                max_age,
            )
        ]