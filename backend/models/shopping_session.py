from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class ShoppingSession(Base):

    __tablename__ = "shopping_sessions"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    session_token = Column(
        String,
        unique=True,
        index=True
    )

    source = Column(
        String
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    ended_at = Column(
        DateTime(timezone=True)
    )

    user = relationship("User")