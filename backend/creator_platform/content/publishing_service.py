from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class PublishingService:
    """
    Handles creator content publication.

    Actual database persistence and feed distribution should
    be performed by the application's repository/event layer.
    """

    @staticmethod
    def _utcnow() -> datetime:
        return datetime.now(timezone.utc)

    @classmethod
    def publish(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        if not content.get("creator_id"):
            raise ValueError(
                "Creator is required."
            )

        current_status = content.get(
            "status"
        )

        if current_status == "published":
            raise ValueError(
                "Content is already published."
            )

        if current_status not in {
            "draft",
            "ready",
            "scheduled",
        }:
            raise ValueError(
                f"Content cannot be published "
                f"from status '{current_status}'."
            )

        # Basic content validation.
        content_type = content.get(
            "content_type"
        )

        if content_type in {
            "video",
            "short",
            "photo",
        }:
            if not content.get("media_url"):
                raise ValueError(
                    "Media is required."
                )

        now = cls._utcnow()

        content["status"] = "published"
        content["published_at"] = now
        content["updated_at"] = now

        # Remove stale scheduling information.
        content.pop(
            "scheduled_at",
            None,
        )

        return content

    @classmethod
    def unpublish(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        if content.get("status") != "published":
            raise ValueError(
                "Only published content can be unpublished."
            )

        content["status"] = "archived"
        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def can_publish(
        cls,
        content: dict[str, Any],
    ) -> bool:

        status = content.get("status")

        return status in {
            "draft",
            "ready",
            "scheduled",
        }