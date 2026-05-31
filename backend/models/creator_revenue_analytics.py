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


class CreatorRevenueAnalytics(Base):

    __tablename__ = "creator_revenue_analytics"

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

    subscription_revenue = Column(
        Float,
        default=0
    )

    affiliate_revenue = Column(
        Float,
        default=0
    )

    sponsorship_revenue = Column(
        Float,
        default=0
    )

    merchandise_revenue = Column(
        Float,
        default=0
    )

    ticket_revenue = Column(
        Float,
        default=0
    )

    total_revenue = Column(
        Float,
        default=0
    )

    period_start = Column(
        DateTime(timezone=True)
    )

    period_end = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        back_populates="creator_revenue_analytics"
    )