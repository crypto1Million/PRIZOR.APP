# backend/lifestyle_commerce/event_tickets.py

class EventTickets:

    def create_event(
        self,
        creator_id: int,
        title: str,
        location: str
    ):

        return {
            "creator_id": creator_id,
            "title": title,
            "location": location
        }

    def get_upcoming_events(self):

        return []


event_tickets = EventTickets()