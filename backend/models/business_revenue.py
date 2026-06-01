from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class BusinessRevenue(Base):

    __tablename__ = "business_revenues"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id"),
        nullable=False
    )

    revenue_source = Column(
        String
    )

    gross_revenue = Column(
        Float,
        default=0
    )

    platform_fee = Column(
        Float,
        default=0
    )

    net_revenue = Column(
        Float,
        default=0
    )

    currency = Column(
        String,
        default="USD"
    )

    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship(
        "BrandProfile"
    )