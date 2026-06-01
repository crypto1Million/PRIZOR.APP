from datetime import datetime
import uuid


class EventTicketing:

    def generate_ticket(
        self,
        user_id: int,
        event_id: int
    ):

        return {
            "ticket_code": str(uuid.uuid4()),
            "user_id": user_id,
            "event_id": event_id,
            "issued_at": datetime.utcnow()
        }

    def validate_ticket(
        self,
        ticket_code: str
    ):

        return True

    def refund_ticket(
        self,
        ticket_code: str
    ):

        return True


event_ticketing = EventTicketing()