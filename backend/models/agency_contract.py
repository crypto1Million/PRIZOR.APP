from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class AgencyContract(Base):

    __tablename__ = "agency_contracts"

    id = Column(Integer, primary_key=True)

    agency_id = Column(
        Integer,
        ForeignKey("agencies.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    revenue_share_percent = Column(
        Float,
        default=20
    )

    status = Column(
        String,
        default="pending"
    )

    terms = Column(Text)

    signed_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    agency = relationship("Agency")
    creator = relationship("User")