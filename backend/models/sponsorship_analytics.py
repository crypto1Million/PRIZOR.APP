from sqlalchemy import (
    Column, Integer, Float,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SponsorshipAnalytics(Base):

    __tablename__ = "sponsorship_analytics"

    id = Column(Integer, primary_key=True, index=True)

    sponsorship_id = Column(
        Integer,
        ForeignKey("sponsorships.id"),
        nullable=False
    )

    impressions = Column(
        Integer,
        default=0
    )

    clicks = Column(
        Integer,
        default=0
    )

    conversions = Column(
        Integer,
        default=0
    )

    engagement_rate = Column(
        Float,
        default=0
    )

    roi = Column(
        Float,
        default=0
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    sponsorship = relationship("Sponsorship")