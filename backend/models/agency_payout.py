from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class AgencyPayout(Base):

    __tablename__ = "agency_payouts"

    id = Column(Integer, primary_key=True)

    agency_id = Column(
        Integer,
        ForeignKey("agencies.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    amount = Column(
        Float,
        default=0
    )

    currency = Column(
        String,
        default="USD"
    )

    status = Column(
        String,
        default="pending"
    )

    paid_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    agency = relationship("Agency")
    creator = relationship("User")