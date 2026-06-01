from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class AdCampaign(Base):
    __tablename__ = "ad_campaigns"

    id = Column(Integer, primary_key=True)

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    title = Column(String)

    budget = Column(Float, default=0)

    status = Column(
        String,
        default="active"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship("BrandProfile")