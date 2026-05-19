from pydantic import BaseModel

class MatchOut(BaseModel):
    user1_id: str
    user2_id: str

    class Config:
        from_attributes = True