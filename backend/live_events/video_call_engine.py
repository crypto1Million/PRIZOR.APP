from datetime import datetime


class VideoCallEngine:

    def create_call(
        self,
        caller_id: int,
        receiver_id: int
    ):

        return {
            "caller_id": caller_id,
            "receiver_id": receiver_id,
            "status": "ringing",
            "created_at": datetime.utcnow().isoformat()
        }

    def accept_call(self, call_id: str):

        return {
            "call_id": call_id,
            "status": "active"
        }

    def end_call(self, call_id: str):

        return {
            "call_id": call_id,
            "status": "ended"
        }


video_call_engine = VideoCallEngine()