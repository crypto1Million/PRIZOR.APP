from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class RevenueSnapshot(Base):

    __tablename__ = "revenue_snapshots"

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

    total_lifetime_revenue = Column(
        Float,
        default=0
    )

    monthly_revenue = Column(
        Float,
        default=0
    )

    weekly_revenue = Column(
        Float,
        default=0
    )

    daily_revenue = Column(
        Float,
        default=0
    )

    pending_payouts = Column(
        Float,
        default=0
    )

    total_payouts = Column(
        Float,
        default=0
    )

    snapshot_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")