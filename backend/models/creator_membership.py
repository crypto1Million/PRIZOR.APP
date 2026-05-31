# backend/models/creator_membership.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorMembership(Base):
    """
    Creator Membership Tiers

    Examples:

    Bronze
    Silver
    Gold
    VIP
    Founder
    """

    __tablename__ = "creator_memberships"

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

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        Text
    )

    price = Column(
        Float,
        nullable=False,
        default=0.0
    )

    billing_cycle = Column(
        String,
        default="monthly"
    )
    # monthly
    # yearly
    # lifetime

    max_members = Column(
        Integer,
        default=0
    )

    current_members = Column(
        Integer,
        default=0
    )

    perks = Column(
        Text
    )

    badge_name = Column(
        String
    )

    badge_color = Column(
        String
    )

    private_chat_access = Column(
        Boolean,
        default=False
    )

    premium_content_access = Column(
        Boolean,
        default=False
    )

    livestream_access = Column(
        Boolean,
        default=False
    )

    event_access = Column(
        Boolean,
        default=False
    )

    merchandise_discount = Column(
        Float,
        default=0.0
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )

    # ====================================
    # RELATIONSHIPS
    # ====================================

    creator = relationship(
        "User",
        back_populates="creator_memberships"
    )