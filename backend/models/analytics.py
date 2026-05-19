from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.database import Base


class AnalyticsEvent(Base):

    __tablename__ = "analytics_events"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String)

    event_type = Column(String)

    event_metadata = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )