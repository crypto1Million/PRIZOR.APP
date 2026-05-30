from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class EventTicket(Base):
    __tablename__ = "event_tickets"

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)

    description = Column(Text)

    location = Column(String)

    ticket_price = Column(Float)

    capacity = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())