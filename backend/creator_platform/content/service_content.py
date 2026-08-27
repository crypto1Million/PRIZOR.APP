from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from sqlalchemy.orm import Session


class ContentService:
    """
    Core Creator Content service.

    Handles the lifecycle of creator content:

        CREATE
          ↓
        DRAFT
          ↓
       READY
          ↓
     SCHEDULED
          ↓
      PUBLISHED
          ↓
      ARCHIVED
    """

    VALID_TYPES = {
        "post",
        "photo",
        "video",
        "short",
        "stream",
    }

    VALID_STATUSES = {
        "draft",
        "processing",
        "ready",
        "scheduled",
        "published",
        "archived",
        "failed",
    }

    @staticmethod
    def _utcnow() -> datetime:
        return datetime.now(timezone.utc)

    @classmethod
    def validate_content_type(
        cls,
        content_type: str,
    ) -> str:

        content_type = (
            content_type
            .strip()
            .lower()
        )

        if content_type not in cls.VALID_TYPES:
            raise ValueError(
                f"Unsupported content type: "
                f"{content_type}"
            )

        return content_type

    @classmethod
    def create_content(
        cls,
        db: Session,
        creator_id: int,
        content_type: str,
        title: str | None = None,
        description: str | None = None,
        media_url: str | None = None,
        thumbnail_url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        content_type = cls.validate_content_type(
            content_type
        )

        if not creator_id:
            raise ValueError(
                "creator_id is required"
            )

        content_id = str(uuid4())

        content = {
            "id": content_id,
            "creator_id": creator_id,
            "content_type": content_type,
            "title": title,
            "description": description,
            "media_url": media_url,
            "thumbnail_url": thumbnail_url,
            "status": "draft",
            "metadata": metadata or {},
            "created_at": cls._utcnow(),
            "updated_at": cls._utcnow(),
        }

        return content

    @classmethod
    def validate_for_publish(
        cls,
        content: dict[str, Any],
    ) -> tuple[bool, list[str]]:

        errors: list[str] = []

        if not content.get("creator_id"):
            errors.append(
                "Creator is required."
            )

        if not content.get("content_type"):
            errors.append(
                "Content type is required."
            )

        content_type = content.get(
            "content_type"
        )

        if content_type in {
            "video",
            "short",
            "photo",
        }:
            if not content.get("media_url"):
                errors.append(
                    "Media is required."
                )

        if content.get("status") == "published":
            errors.append(
                "Content has already been published."
            )

        return (
            len(errors) == 0,
            errors,
        )

    @classmethod
    def update_content(
        cls,
        content: dict[str, Any],
        updates: dict[str, Any],
    ) -> dict[str, Any]:

        protected_fields = {
            "id",
            "creator_id",
            "created_at",
        }

        allowed_fields = {
            "title",
            "description",
            "media_url",
            "thumbnail_url",
            "metadata",
        }

        for field, value in updates.items():

            if field in protected_fields:
                continue

            if field in allowed_fields:
                content[field] = value

        content["updated_at"] = cls._utcnow()

        return content

    @classmethod
    def archive(
        cls,
        content: dict[str, Any],
    ) -> dict[str, Any]:

        if content.get("status") == "published":
            content["status"] = "archived"

        else:
            content["status"] = "archived"

        content["updated_at"] = cls._utcnow()

        return content