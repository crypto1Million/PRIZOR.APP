class AICompanionMemory(Base):
    __tablename__ = "ai_companion_memory"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    communication_style = Column(String)
    comfort_level = Column(String)
    support_preference = Column(String)