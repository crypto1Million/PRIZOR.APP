from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)

    subscriber_id = Column(Integer, ForeignKey("users.id"))

    creator_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)