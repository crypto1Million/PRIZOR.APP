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


class AgencyCreator(Base):

    __tablename__ = "agency_creators"

    id = Column(Integer, primary_key=True)

    agency_id = Column(
        Integer,
        ForeignKey("agencies.id")
    )

    creator_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    status = Column(
        String,
        default="active"
    )

    onboarded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    agency = relationship("Agency")
    creator = relationship("User")