from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Base


class Video(Base):
    """
    Creator video model.

    Supports:
    - Short-form videos
    - Long-form videos
    - Drafts
    - Scheduling
    - Video processing
    - Captions
    - Thumbnails
    - Copyright scanning
    - Creator monetization analytics
    """

    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    creator_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    media_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey(
            "media.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )

    title: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    video_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="video",
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="draft",
        index=True,
    )

    visibility: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="public",
        index=True,
    )

    video_url: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    thumbnail_url: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    duration_seconds: Mapped[Optional[float]] = mapped_column(
        Float,
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

    processing_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending",
        index=True,
    )

    processing_error: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    captions_url: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    ai_caption: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    copyright_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending",
        index=True,
    )

    copyright_score: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True,
    )

    is_monetized: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    scheduled_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        index=True,
    )

    published_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        index=True,
    )

    views_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    likes_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    comments_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    shares_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    saves_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    watch_time_seconds: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
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

    creator = relationship(
        "User",
        foreign_keys=[creator_id],
    )

    media = relationship(
        "Media",
        foreign_keys=[media_id],
    )

    def mark_processing(self) -> None:
        self.processing_status = "processing"
        self.status = "processing"
        self.updated_at = datetime.now(timezone.utc)

    def mark_ready(self) -> None:
        self.processing_status = "ready"
        self.status = "ready"
        self.processing_error = None
        self.updated_at = datetime.now(timezone.utc)

    def mark_failed(
        self,
        error: str,
    ) -> None:

        self.processing_status = "failed"
        self.status = "failed"
        self.processing_error = error
        self.updated_at = datetime.now(timezone.utc)

    def publish(self) -> None:

        if self.processing_status != "ready":
            raise ValueError(
                "Video must be ready before publishing."
            )

        if self.copyright_status == "blocked":
            raise ValueError(
                "Copyright status prevents publication."
            )

        now = datetime.now(timezone.utc)

        self.status = "published"
        self.published_at = now
        self.scheduled_at = None
        self.updated_at = now

    def schedule(
        self,
        scheduled_at: datetime,
    ) -> None:

        if scheduled_at.tzinfo is None:
            scheduled_at = scheduled_at.replace(
                tzinfo=timezone.utc
            )

        if scheduled_at <= datetime.now(timezone.utc):
            raise ValueError(
                "scheduled_at must be in the future."
            )

        if self.processing_status != "ready":
            raise ValueError(
                "Video must be ready before scheduling."
            )

        self.status = "scheduled"
        self.scheduled_at = scheduled_at
        self.updated_at = datetime.now(timezone.utc)

    def archive(self) -> None:

        self.status = "archived"
        self.updated_at = datetime.now(timezone.utc)

    def __repr__(self) -> str:
        return (
            f"<Video id={self.id} "
            f"creator_id={self.creator_id} "
            f"status={self.status}>"
        )