from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class CampaignAsset(Base):
    __tablename__ = "campaign_assets"

    id = Column(Integer, primary_key=True)

    campaign_id = Column(
        Integer,
        ForeignKey("business_campaigns.id")
    )

    asset_type = Column(String)

    asset_url = Column(Text)

    campaign = relationship("BusinessCampaign")