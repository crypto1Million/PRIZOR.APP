from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    String,
    Boolean
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CreatorSubscription(Base):

    __tablename__ = "creator_subscriptions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    subscriber_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    tier_id = Column(
        Integer,
        ForeignKey("subscription_tiers.id"),
        nullable=False
    )

    status = Column(
        String,
        default="active"
    )

    auto_renew = Column(
        Boolean,
        default=True
    )

    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    expires_at = Column(
        DateTime(timezone=True)
    )

    tier = relationship("SubscriptionTier")