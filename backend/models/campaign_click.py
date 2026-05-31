from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class CampaignClick(Base):

    __tablename__ = "campaign_clicks"

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

    ip_address = Column(
        String
    )

    country = Column(
        String
    )

    device_type = Column(
        String
    )

    clicked_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    campaign = relationship("Campaign")