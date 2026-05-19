from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    age: int
    bio: str = ""
    location: str = ""

class SwipeCreate(BaseModel):
    to_user: str
    action: str

class MessageCreate(BaseModel):
    receiver_id: str
    content: str