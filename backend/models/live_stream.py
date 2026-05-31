from sqlalchemy import (
    Column, Integer, String, Text,
    Boolean, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class LiveStream(Base):

    __tablename__ = "live_streams"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(String, nullable=False)

    description = Column(Text)

    category = Column(String)

    thumbnail_url = Column(String)

    stream_key = Column(String, unique=True)

    is_live = Column(Boolean, default=False)

    viewer_count = Column(Integer, default=0)

    started_at = Column(DateTime(timezone=True))

    ended_at = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    creator = relationship("User")