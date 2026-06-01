class EventNotifications:

    def notify_attendees(
        self,
        event_id: int,
        message: str
    ):

        return {
            "event_id": event_id,
            "message": message,
            "sent": True
        }

    def remind_event_start(
        self,
        event_id: int
    ):

        return True

    def notify_cancellation(
        self,
        event_id: int
    ):

        return True


event_notifications = EventNotifications()