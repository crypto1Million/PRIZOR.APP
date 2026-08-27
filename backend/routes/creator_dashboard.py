from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.services.creator_dashboard_service import (
    CreatorDashboardService
)

router = APIRouter(
    prefix="/profile",
    tags=["Creator Dashboard"]
)


@router.get("/{user_id}/creator-dashboard")
def creator_dashboard(
    user_id: int,
    db: Session = Depends(get_db)
):
    dashboard = (
        CreatorDashboardService.get_dashboard(
            db,
            user_id
        )
    )

    if not dashboard:
        raise HTTPException(
            status_code=404,
            detail="Creator not found"
        )

    return dashboard