from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Base


class Post(Base):
    """
    Creator/social post.

    Supports:
    - Text posts
    - Photo posts
    - Multi-media posts
    - Scheduled publishing
    - Drafts
    - Publishing lifecycle
    """

    __tablename__ = "posts"

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

    content: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
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

    archived_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
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

    views_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
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

    def publish(self) -> None:
        now = datetime.now(timezone.utc)

        self.status = "published"
        self.published_at = now
        self.scheduled_at = None
        self.updated_at = now

    def archive(self) -> None:
        now = datetime.now(timezone.utc)

        self.status = "archived"
        self.archived_at = now
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

        self.status = "scheduled"
        self.scheduled_at = scheduled_at
        self.updated_at = datetime.now(timezone.utc)

    def __repr__(self) -> str:
        return (
            f"<Post id={self.id} "
            f"creator_id={self.creator_id} "
            f"status={self.status}>"
        )