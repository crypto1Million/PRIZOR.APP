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


class AgencyCommission(Base):

    __tablename__ = "agency_commissions"

    id = Column(Integer, primary_key=True)

    agency_id = Column(
        Integer,
        ForeignKey("agencies.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    gross_revenue = Column(
        Float,
        default=0
    )

    commission_percent = Column(
        Float,
        default=20
    )

    commission_amount = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    agency = relationship("Agency")
    creator = relationship("User")