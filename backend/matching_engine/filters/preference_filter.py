from __future__ import annotations


class PreferenceFilter:
    """
    Applies high-level dating preferences.

    Hard constraints belong here.
    Soft preferences should be handled by scoring.
    """

    @staticmethod
    def matches(
        candidate,
        preferences: dict,
    ) -> bool:

        # Relationship goal
        preferred_goals = preferences.get(
            "relationship_goals"
        )

        candidate_goal = getattr(
            candidate,
            "relationship_goal",
            None,
        )

        if (
            preferred_goals
            and candidate_goal
            and candidate_goal not in preferred_goals
        ):
            return False

        # Lifestyle
        preferred_lifestyles = preferences.get(
            "lifestyles"
        )

        candidate_lifestyle = getattr(
            candidate,
            "lifestyle",
            None,
        )

        if (
            preferred_lifestyles
            and candidate_lifestyle
            and candidate_lifestyle
            not in preferred_lifestyles
        ):
            return False

        # Smoking
        if preferences.get("non_smoker_only"):
            if getattr(
                candidate,
                "smokes",
                False,
            ):
                return False

        # Drinking
        if preferences.get("non_drinker_only"):
            if getattr(
                candidate,
                "drinks",
                False,
            ):
                return False

        return True

    @classmethod
    def filter(
        cls,
        candidates,
        preferences: dict,
    ):
        return [
            candidate
            for candidate in candidates
            if cls.matches(
                candidate,
                preferences,
            )
        ]