from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class ChemistryPrediction(Base):

    __tablename__ = "chemistry_predictions"

    id = Column(Integer, primary_key=True, index=True)

    user_one_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user_two_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    chemistry_score = Column(
        Float,
        default=0
    )

    chemistry_level = Column(
        String,
        default="medium"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_one = relationship(
        "User",
        foreign_keys=[user_one_id]
    )

    user_two = relationship(
        "User",
        foreign_keys=[user_two_id]
    )