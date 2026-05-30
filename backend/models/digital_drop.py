from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class DigitalDrop(Base):
    __tablename__ = "digital_drops"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)

    description = Column(Text)

    file_url = Column(String)

    price = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())