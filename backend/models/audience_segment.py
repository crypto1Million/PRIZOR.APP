from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class AudienceSegment(Base):

    __tablename__ = "audience_segments"

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

    segment_name = Column(
        String,
        nullable=False
    )

    age_group = Column(
        String
    )

    region = Column(
        String
    )

    interests = Column(
        Text
    )

    fandoms = Column(
        Text
    )

    estimated_size = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship(
        "BrandProfile"
    )