from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class PersonalizationVector(Base):

    __tablename__ = "personalization_vectors"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True
    )

    vector_data = Column(
        Text
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship("User")