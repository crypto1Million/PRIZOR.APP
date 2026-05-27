from sqlalchemy import Column, Integer, String, Text, ForeignKey
from backend.database import Base

class AIProfile(Base):
    __tablename__ = "ai_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    personality_summary = Column(Text)

    interests_summary = Column(Text)

    communication_style = Column(String)

    emotional_profile = Column(String)

    vibe_type = Column(String)