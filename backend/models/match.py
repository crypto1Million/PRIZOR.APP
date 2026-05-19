from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from backend.database import Base
from datetime import datetime


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(String)
    user2_id = Column(String)
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, nullable=True)

    created_at = Column(
       DateTime,
       default=datetime.utcnow
    )