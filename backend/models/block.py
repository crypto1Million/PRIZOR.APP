from sqlalchemy import Column, Integer, ForeignKey
from backend.database import Base

class Block(Base):

    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True, index=True)

    blocker_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    blocked_id = Column(
        Integer,
        ForeignKey("users.id")
    )