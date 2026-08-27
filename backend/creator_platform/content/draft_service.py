from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class DraftService:
    """
    Creator draft management.

    Drafts are content that has not yet been published.
    """

    DRAFT_STATUSES = {
        "draft",
        "processing",
        "ready",
        "failed",
    }

    @staticmethod
    def _utcnow() -> datetime:
        return datetime.now(timezone.utc)

    @classmethod
    def save_draft(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        if not content.get("creator_id"):
            raise ValueError(
                "creator_id is required"
            )

        content["status"] = "draft"
        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def mark_processing(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        content["status"] = "processing"
        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def mark_ready(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        content["status"] = "ready"
        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def mark_failed(
        cls,
        content: dict[str, Any],
        error: str | None = None,
    ) -> dict[str, Any]:

        content["status"] = "failed"

        metadata = content.setdefault(
            "metadata",
            {},
        )

        metadata["processing_error"] = error

        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def prepare_for_publish(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        status = content.get("status")

        if status not in {
            "draft",
            "ready",
        }:
            raise ValueError(
                f"Content with status "
                f"'{status}' cannot be published."
            )

        content["updated_at"] = cls._utcnow()

        return content