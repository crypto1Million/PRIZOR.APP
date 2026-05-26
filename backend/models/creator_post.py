from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class CreatorPost(Base):
    __tablename__ = "creator_posts"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    content = Column(Text)

    media_url = Column(String, nullable=True)

    is_paid = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)