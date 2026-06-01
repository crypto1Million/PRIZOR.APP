from datetime import datetime


class EventRSVP:

    def attend(
        self,
        user_id: int,
        event_id: int
    ):

        return {
            "user_id": user_id,
            "event_id": event_id,
            "status": "going",
            "timestamp": datetime.utcnow()
        }

    def maybe(
        self,
        user_id: int,
        event_id: int
    ):

        return {
            "status": "maybe"
        }

    def decline(
        self,
        user_id: int,
        event_id: int
    ):

        return {
            "status": "declined"
        }


event_rsvp = EventRSVP()