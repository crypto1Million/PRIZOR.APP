class StreamRecording:

    def create_recording(
        self,
        stream_id: int,
        storage_url: str
    ):

        return {
            "stream_id": stream_id,
            "storage_url": storage_url
        }


stream_recording = StreamRecording()