from datetime import datetime


class CallAnalytics:

    def build_call_metrics(
        self,
        call_id: str,
        duration_seconds: int
    ):

        return {
            "call_id": call_id,
            "duration_seconds": duration_seconds,
            "recorded_at": datetime.utcnow().isoformat()
        }


call_analytics = CallAnalytics()