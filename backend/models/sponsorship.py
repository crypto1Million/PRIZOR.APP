from sqlalchemy import (
    Column, Integer, String, Float,
    DateTime, ForeignKey, Text, Boolean
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class Sponsorship(Base):

    __tablename__ = "sponsorships"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    brand_name = Column(String, nullable=False)

    campaign_name = Column(String)

    description = Column(Text)

    budget = Column(Float, default=0)

    status = Column(
        String,
        default="pending"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    starts_at = Column(DateTime(timezone=True))

    ends_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")