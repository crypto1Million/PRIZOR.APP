from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class StreamHighlight(Base):

    __tablename__ = "stream_highlights"

    id = Column(Integer, primary_key=True, index=True)

    stream_id = Column(
        Integer,
        ForeignKey("live_streams.id")
    )

    title = Column(String)

    clip_url = Column(String)

    start_second = Column(Integer)

    end_second = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    stream = relationship("LiveStream")