from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class Tip(Base):
    __tablename__ = "tips"

    id = Column(Integer, primary_key=True, index=True)

    sender_id = Column(Integer, ForeignKey("users.id"))

    creator_id = Column(Integer, ForeignKey("users.id"))

    amount = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)