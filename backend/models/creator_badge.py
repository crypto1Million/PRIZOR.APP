from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorBadge(Base):

    __tablename__ = "creator_badges"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    badge_name = Column(
        String,
        nullable=False
    )

    badge_slug = Column(
        String,
        unique=True,
        nullable=False
    )

    description = Column(
        Text
    )

    icon = Column(
        String
    )

    color = Column(
        String
    )

    rarity = Column(
        String,
        default="common"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    awarded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_badges"
    )