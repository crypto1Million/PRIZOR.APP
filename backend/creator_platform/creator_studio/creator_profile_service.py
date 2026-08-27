from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session


class CreatorProfileService:
    """
    Service responsible for creator profile operations.

    The service intentionally uses attribute-based access instead
    of hard-coding a particular Creator model so it can work with
    the existing Prizor model architecture.
    """

    @staticmethod
    def _get_creator(
        db: Session,
        user_id: int,
    ) -> Any | None:
        """
        Find the creator/profile associated with a user.

        Update the model import/query here if your existing
        codebase uses a dedicated CreatorProfile model.
        """

        try:
            from backend.models.creator_profile import (
                CreatorProfile,
            )
        except ImportError:
            return None

        return (
            db.query(CreatorProfile)
            .filter(
                CreatorProfile.user_id == user_id
            )
            .first()
        )

    @classmethod
    def get_profile(
        cls,
        db: Session,
        user_id: int,
    ) -> dict[str, Any] | None:

        creator = cls._get_creator(
            db,
            user_id,
        )

        if creator is None:
            return None

        return {
            "id": getattr(creator, "id", None),
            "user_id": getattr(
                creator,
                "user_id",
                user_id,
            ),
            "display_name": getattr(
                creator,
                "display_name",
                None,
            ),
            "username": getattr(
                creator,
                "username",
                None,
            ),
            "bio": getattr(
                creator,
                "bio",
                None,
            ),
            "avatar_url": getattr(
                creator,
                "avatar_url",
                None,
            ),
            "banner_url": getattr(
                creator,
                "banner_url",
                None,
            ),
            "is_creator": True,
            "is_verified": getattr(
                creator,
                "is_verified",
                False,
            ),
            "verification_type": getattr(
                creator,
                "verification_type",
                None,
            ),
        }

    @classmethod
    def update_profile(
        cls,
        db: Session,
        user_id: int,
        data: dict[str, Any],
    ) -> dict[str, Any] | None:

        creator = cls._get_creator(
            db,
            user_id,
        )

        if creator is None:
            return None

        allowed_fields = {
            "display_name",
            "username",
            "bio",
            "avatar_url",
            "banner_url",
        }

        for field, value in data.items():

            if field not in allowed_fields:
                continue

            if hasattr(creator, field):
                setattr(
                    creator,
                    field,
                    value,
                )

        db.commit()
        db.refresh(creator)

        return cls.get_profile(
            db,
            user_id,
        )

    @classmethod
    def get_verification_status(
        cls,
        db: Session,
        user_id: int,
    ) -> dict[str, Any]:

        creator = cls._get_creator(
            db,
            user_id,
        )

        if creator is None:
            return {
                "user_id": user_id,
                "is_creator": False,
                "verified": False,
                "verification_type": None,
            }

        return {
            "user_id": user_id,
            "is_creator": True,
            "verified": getattr(
                creator,
                "is_verified",
                False,
            ),
            "verification_type": getattr(
                creator,
                "verification_type",
                None,
            ),
        }