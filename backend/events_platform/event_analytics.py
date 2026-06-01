class EventAnalytics:

    def attendance_metrics(
        self,
        event_id: int
    ):

        return {
            "attendees": 0,
            "checkins": 0
        }

    def engagement_metrics(
        self,
        event_id: int
    ):

        return {
            "messages": 0,
            "reactions": 0
        }

    def revenue_metrics(
        self,
        event_id: int
    ):

        return {
            "ticket_sales": 0,
            "sponsor_revenue": 0
        }


event_analytics = EventAnalytics()