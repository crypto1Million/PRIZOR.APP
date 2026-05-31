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


class SubscriptionInvoice(Base):

    __tablename__ = "subscription_invoices"

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

    invoice_number = Column(
        String,
        unique=True
    )

    amount = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="paid"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    subscription = relationship(
        "CreatorSubscription"
    )