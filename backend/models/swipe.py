from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from backend.database import Base

class Swipe(Base):
    __tablename__ = "swipes"

    id = Column(Integer, primary_key=True, index=True)

    swiper_id = Column(Integer, ForeignKey("users.id"))
    swiped_id = Column(Integer, ForeignKey("users.id"))

    is_like = Column(Boolean)