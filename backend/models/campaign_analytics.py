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


class CampaignAnalytics(Base):

    __tablename__ = "campaign_analytics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.id"),
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

    ctr = Column(
        Float,
        default=0
    )

    conversion_rate = Column(
        Float,
        default=0
    )

    revenue = Column(
        Float,
        default=0
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    campaign = relationship("Campaign")