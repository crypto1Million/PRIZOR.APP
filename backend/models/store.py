from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.sql import func
from backend.database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String, nullable=False)

    description = Column(Text)

    logo_url = Column(String)

    banner_url = Column(String)

    is_active = Column(Integer, default=1)

    created_at = Column(DateTime(timezone=True), server_default=func.now())