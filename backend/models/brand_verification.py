from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class BrandVerification(Base):
    __tablename__ = "brand_verifications"

    id = Column(Integer, primary_key=True, index=True)

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id"),
        nullable=False
    )

    website_verified = Column(Boolean, default=False)

    documents_verified = Column(Boolean, default=False)

    social_verified = Column(Boolean, default=False)

    verification_level = Column(
        String,
        default="pending"
    )

    verified_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    brand = relationship("BrandProfile")