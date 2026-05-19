from pydantic import BaseModel

class MessageCreate(BaseModel):
    receiver_id: int
    content: str

class MessageOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    content: str

    class Config:
        from_attributes = True

class MessageResponse(BaseModel):

    id: int
    content: str

    is_seen: bool
    seen_at: datetime | None

    class Config:
        orm_mode = True        