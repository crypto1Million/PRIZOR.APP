from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SponsoredCommunity(Base):

    __tablename__ = "sponsored_communities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    community_id = Column(
        Integer,
        nullable=False
    )

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id"),
        nullable=False
    )

    sponsorship_type = Column(
        String,
        default="banner"
    )

    sponsorship_fee = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="active"
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

    brand = relationship(
        "BrandProfile"
    )