from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session

from .creator_profile_service import (
    CreatorProfileService,
)

from .creator_settings_service import (
    CreatorSettingsService,
)


class StudioService:
    """
    Main Creator Studio orchestration service.

    Creator Studio should act as the control center for:
        - profile
        - content
        - drafts
        - scheduling
        - analytics
        - monetization
        - AI tools
    """

    @classmethod
    def get_dashboard(
        cls,
        db: Session,
        user_id: int,
    ) -> dict[str, Any]:

        profile = (
            CreatorProfileService.get_profile(
                db,
                user_id,
            )
        )

        if profile is None:
            return {
                "creator": False,
                "user_id": user_id,
            }

        verification = (
            CreatorProfileService
            .get_verification_status(
                db,
                user_id,
            )
        )

        settings = (
            CreatorSettingsService
            .get_defaults()
        )

        return {
            "creator": True,
            "user_id": user_id,

            "profile": profile,

            "verification": verification,

            "settings": settings,

            "studio": {
                "content": {
                    "drafts": 0,
                    "scheduled": 0,
                    "published": 0,
                },

                "analytics": {
                    "views": 0,
                    "likes": 0,
                    "comments": 0,
                    "shares": 0,
                    "followers_gained": 0,
                },

                "monetization": {
                    "revenue": 0,
                    "pending_balance": 0,
                    "available_balance": 0,
                },

                "ai": {
                    "insights_available": True,
                    "caption_generation": True,
                    "content_optimization": True,
                },
            },
        }

    @classmethod
    def get_creator_overview(
        cls,
        db: Session,
        user_id: int,
    ) -> dict[str, Any]:

        dashboard = cls.get_dashboard(
            db,
            user_id,
        )

        if not dashboard.get("creator"):
            return dashboard

        return {
            "user_id": user_id,
            "profile": dashboard["profile"],
            "verification": dashboard[
                "verification"
            ],
            "analytics": dashboard[
                "studio"
            ]["analytics"],
            "monetization": dashboard[
                "studio"
            ]["monetization"],
        }

    @classmethod
    def check_creator_access(
        cls,
        db: Session,
        user_id: int,
    ) -> bool:

        profile = (
            CreatorProfileService.get_profile(
                db,
                user_id,
            )
        )

        return profile is not None

    @classmethod
    def check_monetization_access(
        cls,
        db: Session,
        user_id: int,
    ) -> bool:

        verification = (
            CreatorProfileService
            .get_verification_status(
                db,
                user_id,
            )
        )

        return (
            verification["is_creator"]
            and verification["verified"]
        )