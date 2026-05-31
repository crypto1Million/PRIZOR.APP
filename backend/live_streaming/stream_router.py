class StreamRouter:

    def build_channel(
        self,
        stream_id: int
    ):

        return f"stream:{stream_id}"


stream_router = StreamRouter()