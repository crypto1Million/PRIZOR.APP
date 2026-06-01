from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class CreatorPartnership(Base):
    __tablename__ = "creator_partnerships"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    status = Column(
        String,
        default="pending"
    )

    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship(
        "User",
        foreign_keys=[creator_id]
    )

    brand = relationship("BrandProfile")