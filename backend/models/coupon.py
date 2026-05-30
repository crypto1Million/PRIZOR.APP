from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, unique=True)

    discount_percent = Column(Float)

    max_uses = Column(Integer)

    current_uses = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())