from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SubscriptionPayment(Base):

    __tablename__ = "subscription_payments"

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

    amount = Column(
        Float,
        default=0
    )

    currency = Column(
        String,
        default="USD"
    )

    payment_method = Column(
        String
    )

    status = Column(
        String,
        default="completed"
    )

    paid_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    subscription = relationship(
        "CreatorSubscription"
    )