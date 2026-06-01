from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class AdImpression(Base):
    __tablename__ = "ad_impressions"

    id = Column(Integer, primary_key=True)

    ad_campaign_id = Column(
        Integer,
        ForeignKey("ad_campaigns.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    ad_campaign = relationship("AdCampaign")