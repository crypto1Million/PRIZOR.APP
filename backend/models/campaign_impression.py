from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CampaignImpression(Base):

    __tablename__ = "campaign_impressions"

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

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    source = Column(
        String
    )

    device_type = Column(
        String
    )

    country = Column(
        String
    )

    viewed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    campaign = relationship("Campaign")