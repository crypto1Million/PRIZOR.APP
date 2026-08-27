from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class SchedulingService:
    """
    Creator content scheduling.

    Scheduling does not publish content immediately.

    Celery/worker infrastructure should later call
    PublishingService.publish() when scheduled_at is reached.
    """

    @staticmethod
    def _utcnow() -> datetime:
        return datetime.now(timezone.utc)

    @classmethod
    def schedule(
        cls,
        content: dict[str, Any],
        scheduled_at: datetime,
    ) -> dict[str, Any]:

        if scheduled_at.tzinfo is None:
            scheduled_at = scheduled_at.replace(
                tzinfo=timezone.utc
            )

        now = cls._utcnow()

        if scheduled_at <= now:
            raise ValueError(
                "scheduled_at must be in the future."
            )

        if not content.get("creator_id"):
            raise ValueError(
                "Creator is required."
            )

        if content.get("status") not in {
            "draft",
            "ready",
        }:
            raise ValueError(
                "Only draft or ready content "
                "can be scheduled."
            )

        content["scheduled_at"] = scheduled_at
        content["status"] = "scheduled"
        content["updated_at"] = now

        return content

    @classmethod
    def cancel_schedule(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        if content.get("status") != "scheduled":
            raise ValueError(
                "Content is not scheduled."
            )

        content.pop(
            "scheduled_at",
            None,
        )

        content["status"] = "draft"
        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def is_due(
        cls,
        content: dict[str, Any],
    ) -> bool:

        if content.get("status") != "scheduled":
            return False

        scheduled_at = content.get(
            "scheduled_at"
        )

        if not scheduled_at:
            return False

        if scheduled_at.tzinfo is None:
            scheduled_at = scheduled_at.replace(
                tzinfo=timezone.utc
            )

        return scheduled_at <= cls._utcnow()