from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SubscriptionRenewal(Base):

    __tablename__ = "subscription_renewals"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    subscription_id = Column(
        Integer,
        ForeignKey("creator_subscriptions.id"),
        nullable=False
    )

    successful = Column(
        Boolean,
        default=True
    )

    renewed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    next_renewal = Column(
        DateTime(timezone=True)
    )

    subscription = relationship(
        "CreatorSubscription"
    )