from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class BrandCampaign(Base):

    __tablename__ = "brand_campaigns"

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

    name = Column(
        String,
        nullable=False
    )

    slug = Column(
        String,
        unique=True,
        index=True
    )

    description = Column(
        Text
    )

    objective = Column(
        String,
        default="awareness"
    )

    campaign_type = Column(
        String,
        default="sponsored_post"
    )

    budget = Column(
        Float,
        default=0
    )

    spent = Column(
        Float,
        default=0
    )

    impressions = Column(
        Integer,
        default=0
    )

    clicks = Column(
        Integer,
        default=0
    )

    conversions = Column(
        Integer,
        default=0
    )

    active = Column(
        Boolean,
        default=True
    )

    starts_at = Column(
        DateTime(timezone=True)
    )

    ends_at = Column(
        DateTime(timezone=True)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )

    brand = relationship(
        "BrandProfile"
    )