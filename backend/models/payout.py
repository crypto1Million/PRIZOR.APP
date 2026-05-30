from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class Payout(Base):
    __tablename__ = "payouts"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    amount = Column(Float)

    payout_method = Column(String)

    status = Column(String, default="pending")

    transaction_id = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())