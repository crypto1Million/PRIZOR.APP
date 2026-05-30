from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    store_id = Column(Integer, ForeignKey("stores.id"))

    name = Column(String, nullable=False)

    description = Column(Text)

    image_url = Column(String)

    price = Column(Float, nullable=False)

    inventory = Column(Integer, default=0)

    category = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())