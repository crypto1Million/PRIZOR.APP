from sqlalchemy import Column, Integer, ForeignKey
from backend.database import Base

class CommunityMember(Base):
    __tablename__ = "community_members"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    community_id = Column(Integer, ForeignKey("communities.id"))