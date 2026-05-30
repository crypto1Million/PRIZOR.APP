from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer, default=1)

    created_at = Column(DateTime(timezone=True), server_default=func.now())