from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime,
    Boolean,
    Text,
    Table,
    UniqueConstraint,
    Index,
    func,
    Enum,
    ARRAY,
    JSON,
)

from sqlalchemy.orm import relationship
from backend.database import Base

class SubscriptionTier(Base):
    __tablename__ = "subscription_tiers"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String, nullable=False)

    monthly_price = Column(Float)

    perks = Column(JSON)

    benefits = relationship(
    "SubscriptionBenefit"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    creator = relationship(
        "User",
        back_populates="subscription_tiers"
    )

    
