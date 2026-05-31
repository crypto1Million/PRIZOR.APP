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


class CampaignConversion(Base):

    __tablename__ = "campaign_conversions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    conversion_type = Column(
        String
    )

    conversion_value = Column(
        Float,
        default=0
    )

    converted_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    campaign = relationship("Campaign")