from datetime import datetime


class StreamEngine:

    def start_stream(
        self,
        creator_id: int,
        title: str,
        category: str
    ):

        return {
            "creator_id": creator_id,
            "title": title,
            "category": category,
            "status": "live",
            "started_at": datetime.utcnow().isoformat()
        }

    def end_stream(
        self,
        stream_id: int
    ):

        return {
            "stream_id": stream_id,
            "status": "ended"
        }


stream_engine = StreamEngine()