from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
import uuid
from database import Base

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    age = Column(Integer)
    bio = Column(String)
    location = Column(String)

    # 🔥 ADD THIS
    profile_pic = Column(String, nullable=True)

class Swipe(Base):
    __tablename__ = "swipes"

    id = Column(String, primary_key=True, default=generate_uuid)
    from_user = Column(String, ForeignKey("users.id"))
    to_user = Column(String, ForeignKey("users.id"))
    action = Column(String)  # like / dislike
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Match(Base):
    __tablename__ = "matches"

    id = Column(String, primary_key=True, default=generate_uuid)
    user1 = Column(String)
    user2 = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=generate_uuid)
    sender_id = Column(String)
    receiver_id = Column(String)
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())