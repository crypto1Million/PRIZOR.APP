from datetime import datetime


class EventChat:

    def send_message(
        self,
        event_id: int,
        user_id: int,
        message: str
    ):

        return {
            "event_id": event_id,
            "user_id": user_id,
            "message": message,
            "created_at": datetime.utcnow()
        }

    def get_messages(
        self,
        event_id: int
    ):

        return []

    def delete_message(
        self,
        message_id: int
    ):

        return True


event_chat = EventChat()