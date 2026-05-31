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


class CommissionReport(Base):

    __tablename__ = "commission_reports"

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

    report_period = Column(
        String
    )
    # daily
    # weekly
    # monthly

    total_affiliate_commission = Column(
        Float,
        default=0
    )

    total_referral_commission = Column(
        Float,
        default=0
    )

    total_commission = Column(
        Float,
        default=0
    )

    generated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")