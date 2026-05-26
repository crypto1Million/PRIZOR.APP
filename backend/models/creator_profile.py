from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from backend.database import Base

class CreatorProfile(Base):
    __tablename__ = "creator_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    display_name = Column(String)

    bio = Column(Text)

    category = Column(String)

    subscription_price = Column(Integer, default=0)

    is_verified_creator = Column(Boolean, default=False)

    banner_image = Column(String, nullable=True)