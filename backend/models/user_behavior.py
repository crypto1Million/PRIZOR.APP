from sqlalchemy import Column, Integer, ForeignKey
from backend.database import Base

class UserBehavior(Base):
    __tablename__ = "user_behavior" 

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    target_user_id = Column(Integer, ForeignKey("users.id"))

    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)