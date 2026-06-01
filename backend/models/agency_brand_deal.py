from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class AgencyBrandDeal(Base):

    __tablename__ = "agency_brand_deals"

    id = Column(Integer, primary_key=True)

    agency_id = Column(
        Integer,
        ForeignKey("agencies.id")
    )

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    deal_value = Column(
        Float,
        default=0
    )

    campaign_name = Column(String)

    description = Column(Text)

    status = Column(
        String,
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    agency = relationship("Agency")
    brand = relationship("BrandProfile")
    creator = relationship("User")