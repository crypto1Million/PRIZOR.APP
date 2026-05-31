from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey, Boolean
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class SponsorshipDeliverable(Base):

    __tablename__ = "sponsorship_deliverables"

    id = Column(Integer, primary_key=True, index=True)

    sponsorship_id = Column(
        Integer,
        ForeignKey("sponsorships.id"),
        nullable=False
    )

    deliverable_type = Column(String)

    title = Column(String)

    due_date = Column(DateTime(timezone=True))

    completed = Column(
        Boolean,
        default=False
    )

    completed_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sponsorship = relationship("Sponsorship")