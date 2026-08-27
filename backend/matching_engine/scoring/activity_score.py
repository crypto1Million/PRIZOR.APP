from __future__ import annotations

from datetime import datetime, timezone
from math import exp


class ActivityScore:
    """
    Calculates profile activity quality.

    Parameters:
        last_active_at:
            Last activity timestamp.

        interactions_30d:
            Number of meaningful interactions during
            the previous 30 days.

        posts_30d:
            Number of posts created during the
            previous 30 days.
    """

    @staticmethod
    def calculate(
        last_active_at: datetime | None,
        interactions_30d: int = 0,
        posts_30d: int = 0,
    ) -> float:

        if interactions_30d < 0:
            interactions_30d = 0

        if posts_30d < 0:
            posts_30d = 0

        # Recency component.
        if last_active_at is None:
            recency_score = 0.0
        else:
            if last_active_at.tzinfo is None:
                last_active_at = last_active_at.replace(
                    tzinfo=timezone.utc
                )

            now = datetime.now(timezone.utc)

            age_hours = max(
                0.0,
                (
                    now - last_active_at
                ).total_seconds() / 3600,
            )

            recency_score = (
                100.0
                * exp(-age_hours / 72.0)
            )

        # Engagement component.
        interaction_score = min(
            100.0,
            interactions_30d / 100.0 * 100.0,
        )

        # Content activity.
        content_score = min(
            100.0,
            posts_30d / 20.0 * 100.0,
        )

        score = (
            recency_score * 0.50
            + interaction_score * 0.30
            + content_score * 0.20
        )

        return round(
            max(0.0, min(100.0, score)),
            4,
        )