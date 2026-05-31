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


class CommissionPayout(Base):

    __tablename__ = "commission_payouts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    commission_id = Column(
        Integer,
        ForeignKey("commissions.id"),
        nullable=False
    )

    amount = Column(
        Float,
        default=0
    )

    payout_method = Column(
        String
    )

    transaction_reference = Column(
        String
    )

    status = Column(
        String,
        default="pending"
    )

    paid_at = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    commission = relationship("Commission")