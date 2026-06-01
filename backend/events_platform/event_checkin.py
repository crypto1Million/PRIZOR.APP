from datetime import datetime


class EventCheckin:

    def checkin(
        self,
        user_id: int,
        event_id: int
    ):

        return {
            "user_id": user_id,
            "event_id": event_id,
            "checked_in": True,
            "timestamp": datetime.utcnow()
        }

    def checkout(
        self,
        user_id: int,
        event_id: int
    ):

        return {
            "checked_out": True
        }


event_checkin = EventCheckin()