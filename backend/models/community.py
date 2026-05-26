from sqlalchemy import Column, String, Integer, Text, Boolean, ForeignKey
from backend.database import Base

class Community(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True)

    description = Column(Text)

    avatar = Column(String, nullable=True)

    is_private = Column(Boolean, default=False)

    creator_only = Column(Boolean, default=False)

    subscription_required = Column(Boolean, default=False)

    creator_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    required_tier_id = Column(Integer, ForeignKey("subscription_tiers.id"), nullable=True)