from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class BrandAnalytics(Base):
    __tablename__ = "brand_analytics"

    id = Column(Integer, primary_key=True, index=True)

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    impressions = Column(Integer, default=0)

    clicks = Column(Integer, default=0)

    conversions = Column(Integer, default=0)

    revenue = Column(Float, default=0)

    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship("BrandProfile")