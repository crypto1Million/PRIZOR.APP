from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class AdConversion(Base):
    __tablename__ = "ad_conversions"

    id = Column(Integer, primary_key=True)

    ad_campaign_id = Column(
        Integer,
        ForeignKey("ad_campaigns.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    value = Column(Float, default=0)

    converted_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    ad_campaign = relationship("AdCampaign")