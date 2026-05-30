from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer, default=1)

    total_amount = Column(Float)

    status = Column(String, default="pending")

    created_at = Column(DateTime(timezone=True), server_default=func.now())