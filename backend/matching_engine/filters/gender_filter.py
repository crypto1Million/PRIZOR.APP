from __future__ import annotations


class GenderFilter:
    """
    Filters candidates according to the user's
    selected gender preferences.
    """

    @staticmethod
    def matches(
        candidate_gender: str | None,
        preferred_genders: set[str] | list[str] | tuple[str, ...],
    ) -> bool:

        if not candidate_gender:
            return False

        normalized_gender = (
            candidate_gender.strip().lower()
        )

        normalized_preferences = {
            str(gender).strip().lower()
            for gender in preferred_genders
            if gender
        }

        if not normalized_preferences:
            return True

        return (
            normalized_gender
            in normalized_preferences
        )

    @classmethod
    def filter(
        cls,
        candidates,
        preferred_genders,
    ):
        return [
            candidate
            for candidate in candidates
            if cls.matches(
                getattr(candidate, "gender", None),
                preferred_genders,
            )
        ]