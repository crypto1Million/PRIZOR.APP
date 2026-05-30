from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(Text)

    logo_url = Column(String)

    website = Column(String)

    category = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())