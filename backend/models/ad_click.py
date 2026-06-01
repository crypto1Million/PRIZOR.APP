from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class AdClick(Base):
    __tablename__ = "ad_clicks"

    id = Column(Integer, primary_key=True)

    ad_campaign_id = Column(
        Integer,
        ForeignKey("ad_campaigns.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    clicked_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    ad_campaign = relationship("AdCampaign")