from sqlalchemy import Column, Integer, Float, ForeignKey
from backend.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    balance = Column(Float, default=0.0)

    creator_earnings = Column(Float, default=0.0)