from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db

router = APIRouter(
    prefix="/profile",
    tags=["AI Insights"]
)


@router.get("/{user_id}/ai-insights")
def ai_insights(
    user_id: int,
    db: Session = Depends(get_db)
):
    return {
        "user_id": user_id,

        "personality": "Builder",

        "top_interests": [
            "Crypto",
            "Startups",
            "Fitness"
        ],

        "relationship_style":
            "Ambitious",

        "creator_score": 88,

        "community_score": 91
    }