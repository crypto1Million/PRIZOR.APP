class EventModeration:

    def remove_attendee(
        self,
        event_id: int,
        user_id: int
    ):

        return True

    def mute_user(
        self,
        event_id: int,
        user_id: int
    ):

        return True

    def report_user(
        self,
        event_id: int,
        reporter_id: int,
        reported_id: int,
        reason: str
    ):

        return {
            "event_id": event_id,
            "reporter_id": reporter_id,
            "reported_id": reported_id,
            "reason": reason
        }


event_moderation = EventModeration()
