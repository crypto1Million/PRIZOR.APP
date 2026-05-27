from sqlalchemy import Column, Integer, Text, ForeignKey
from backend.database import Base

class MatchInsight(Base):
    __tablename__ = "match_insights"

    id = Column(Integer, primary_key=True, index=True)

    user1_id = Column(Integer, ForeignKey("users.id"))

    user2_id = Column(Integer, ForeignKey("users.id"))

    insight_text = Column(Text)

    compatibility_score = Column(Integer, default=0)