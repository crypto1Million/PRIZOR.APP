from sqlalchemy import Column, Integer, DateTime, String
from backend.database import Base
from datetime import datetime 

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    user1_id = Column(Integer, index=True)
    user2_id = Column(Integer, index=True)

    last_message = Column(String)
    last_message_time = Column(DateTime, default=datetime.utcnow)

    unread_user1 = Column(Integer, default=0)
    unread_user2 = Column(Integer, default=0)