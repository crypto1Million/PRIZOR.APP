from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class AIOnboarding(Base):
    __tablename__ = "ai_onboarding"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    relationship_goal = Column(String)

    social_energy = Column(String)

    communication_style = Column(String)

    community_interests = Column(String)

    emotional_style = Column(String)