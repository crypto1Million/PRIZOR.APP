from datetime import datetime
from typing import Dict, Any


class EventEngine:

    def create_event(
        self,
        title: str,
        description: str,
        creator_id: int,
        event_type: str,
        starts_at: datetime,
        ends_at: datetime,
        location: str | None = None
    ) -> Dict[str, Any]:

        return {
            "title": title,
            "description": description,
            "creator_id": creator_id,
            "event_type": event_type,
            "location": location,
            "starts_at": starts_at,
            "ends_at": ends_at,
            "status": "scheduled",
            "created_at": datetime.utcnow()
        }

    def publish_event(
        self,
        event_id: int
    ) -> Dict[str, Any]:

        return {
            "event_id": event_id,
            "status": "published"
        }

    def cancel_event(
        self,
        event_id: int,
        reason: str
    ) -> Dict[str, Any]:

        return {
            "event_id": event_id,
            "status": "cancelled",
            "reason": reason
        }

    def complete_event(
        self,
        event_id: int
    ) -> Dict[str, Any]:

        return {
            "event_id": event_id,
            "status": "completed"
        }


event_engine = EventEngine()