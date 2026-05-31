from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from sqlalchemy.orm import relationship

from backend.database import Base


class SubscriptionBenefit(Base):

    __tablename__ = "subscription_benefits"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tier_id = Column(
        Integer,
        ForeignKey("subscription_tiers.id"),
        nullable=False
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text
    )

    benefit_type = Column(
        String
    )

    tier = relationship(
        "SubscriptionTier"
    )
    