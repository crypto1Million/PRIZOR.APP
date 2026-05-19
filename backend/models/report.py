from sqlalchemy import Column, Integer, String, DateTime
from backend.database import Base

from datetime import datetime


class Report(Base):

    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)

    reporter_id = Column(Integer)

    reported_user_id = Column(Integer)

    reason = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )