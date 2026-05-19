from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey 
from backend.database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String)
    receiver_id = Column(String)
    content = Column(String)
    is_delivered = Column(Boolean, default=False)
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, nullable=True)
    sent_at = Column(DateTime, default=datetime.utcnow)
    delivered_at = Column(DateTime, nullable=True)    
    is_seen = Column(Boolean, default=False)
    seen_at = Column(DateTime, nullable=True)