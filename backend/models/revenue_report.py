from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    String
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class RevenueReport(Base):

    __tablename__ = "revenue_reports"

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

    report_type = Column(
        String
    )
    # daily
    # weekly
    # monthly
    # yearly

    gross_revenue = Column(
        Float,
        default=0
    )

    net_revenue = Column(
        Float,
        default=0
    )

    platform_fees = Column(
        Float,
        default=0
    )

    payout_amount = Column(
        Float,
        default=0
    )

    generated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")