from pydantic import BaseModel

class ReportCreate(BaseModel):
    user_id: int
    reason: str
    