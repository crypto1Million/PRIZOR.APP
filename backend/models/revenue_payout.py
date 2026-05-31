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


class RevenuePayout(Base):

    __tablename__ = "revenue_payouts"

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

    amount = Column(
        Float,
        default=0
    )

    currency = Column(
        String,
        default="USD"
    )

    payout_method = Column(
        String
    )
    # bank
    # paypal
    # crypto

    payout_reference = Column(
        String
    )

    status = Column(
        String,
        default="pending"
    )

    processed_at = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")