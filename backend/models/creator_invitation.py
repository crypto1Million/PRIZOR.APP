from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class CreatorInvitation(Base):
    __tablename__ = "creator_invitations"

    id = Column(Integer, primary_key=True)

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    message = Column(Text)

    status = Column(
        String,
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship("BrandProfile")

    creator = relationship(
        "User",
        foreign_keys=[creator_id]
    )