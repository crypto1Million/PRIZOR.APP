from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class SubscriptionTier(Base):
    __tablename__ = "subscription_tiers"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String, nullable=False)

    monthly_price = Column(Float)

    perks = Column(String)