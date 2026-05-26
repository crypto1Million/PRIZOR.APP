from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from datetime import datetime
from backend.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    sender_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    amount = Column(Float)

    transaction_type = Column(String)

    payment_provider = Column(String)

    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    token_symbol = Column(String, nullable=True)

    tx_hash = Column(String, nullable=True)

    blockchain = Column(String, nullable=True)