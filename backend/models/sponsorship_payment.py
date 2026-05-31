from sqlalchemy import (
    Column, Integer, Float,
    String, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SponsorshipPayment(Base):

    __tablename__ = "sponsorship_payments"

    id = Column(Integer, primary_key=True, index=True)

    sponsorship_id = Column(
        Integer,
        ForeignKey("sponsorships.id"),
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

    payment_method = Column(String)

    status = Column(
        String,
        default="pending"
    )

    paid_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sponsorship = relationship("Sponsorship")