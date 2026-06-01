from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(String, nullable=False)

    description = Column(Text)

    event_type = Column(String, default="virtual")

    category = Column(String)

    location = Column(String)

    banner_url = Column(Text)

    max_capacity = Column(Integer, default=0)

    is_ticketed = Column(Boolean, default=False)

    status = Column(String, default="draft")

    starts_at = Column(DateTime(timezone=True))

    ends_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")