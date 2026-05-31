from datetime import datetime


class StreamChat:

    def create_message(
        self,
        user_id: int,
        message: str
    ):

        return {
            "user_id": user_id,
            "message": message,
            "created_at": datetime.utcnow().isoformat()
        }


stream_chat = StreamChat()