from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Base


class Media(Base):
    """
    Stores uploaded media assets used by posts, videos,
    profiles, messages, events, and other Prizor features.
    """

    __tablename__ = "media"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    owner_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    media_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    storage_key: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    thumbnail_url: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    mime_type: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )

    filename: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    size_bytes: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        nullable=True,
    )

    width: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )

    height: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )

    duration_seconds: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )

    processing_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending",
        index=True,
    )

    is_public: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationships
    owner = relationship(
        "User",
        foreign_keys=[owner_id],
    )

    def __repr__(self) -> str:
        return (
            f"<Media id={self.id} "
            f"type={self.media_type} "
            f"status={self.processing_status}>"
        )