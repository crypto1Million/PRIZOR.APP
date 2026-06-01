from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class BusinessCampaign(Base):
    __tablename__ = "business_campaigns"

    id = Column(Integer, primary_key=True)

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    name = Column(String)

    description = Column(Text)

    budget = Column(Float, default=0)

    status = Column(
        String,
        default="draft"
    )

    starts_at = Column(DateTime(timezone=True))

    ends_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship("BrandProfile")