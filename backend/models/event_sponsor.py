from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class EventSponsor(Base):

    __tablename__ = "event_sponsors"

    id = Column(Integer, primary_key=True)

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    brand_id = Column(
        Integer,
        ForeignKey("brand_profiles.id")
    )

    sponsorship_amount = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    event = relationship("Event")

    brand = relationship("BrandProfile")