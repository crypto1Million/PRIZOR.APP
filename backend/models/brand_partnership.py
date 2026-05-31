from sqlalchemy import (
    Column, Integer, String,
    Float, DateTime, ForeignKey,
    Boolean, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class BrandPartnership(Base):

    __tablename__ = "brand_partnerships"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    brand_name = Column(
        String,
        nullable=False
    )

    partnership_type = Column(String)

    description = Column(Text)

    total_value = Column(
        Float,
        default=0
    )

    active = Column(
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