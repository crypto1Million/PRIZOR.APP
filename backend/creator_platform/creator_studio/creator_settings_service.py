from __future__ import annotations

from typing import Any


class CreatorSettingsService:
    """
    Manages creator-specific preferences.

    Settings are kept in a separate service so creator settings
    can later be persisted in Redis/PostgreSQL without changing
    the rest of Creator Studio.
    """

    DEFAULTS = {
        "public_email": False,
        "show_revenue": False,
        "allow_tips": True,
        "allow_subscriptions": True,
        "allow_messages": True,
        "auto_captions": True,
        "ai_caption_suggestions": True,
        "copyright_scan": True,
        "content_notifications": True,
        "analytics_notifications": True,
    }

    @classmethod
    def get_defaults(cls) -> dict[str, Any]:
        return dict(cls.DEFAULTS)

    @classmethod
    def normalize(
        cls,
        settings: dict[str, Any] | None,
    ) -> dict[str, Any]:

        result = cls.get_defaults()

        if not settings:
            return result

        for key, value in settings.items():

            if key not in cls.DEFAULTS:
                continue

            if isinstance(
                cls.DEFAULTS[key],
                bool,
            ):
                result[key] = bool(value)
            else:
                result[key] = value

        return result

    @classmethod
    def update(
        cls,
        current_settings: dict[str, Any] | None,
        updates: dict[str, Any],
    ) -> dict[str, Any]:

        settings = cls.normalize(
            current_settings
        )

        for key, value in updates.items():

            if key not in cls.DEFAULTS:
                continue

            settings[key] = value

        return cls.normalize(settings)

    @classmethod
    def can_monetize(
        cls,
        settings: dict[str, Any] | None,
        verified: bool,
    ) -> bool:

        normalized = cls.normalize(
            settings
        )

        if not verified:
            return False

        return (
            normalized["allow_tips"]
            or normalized["allow_subscriptions"]
        )