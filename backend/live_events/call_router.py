from backend.live_events.video_call_engine import (
    video_call_engine
)


class CallRouter:

    def route_call(
        self,
        caller_id: int,
        receiver_id: int
    ):

        return video_call_engine.create_call(
            caller_id,
            receiver_id
        )


call_router = CallRouter()