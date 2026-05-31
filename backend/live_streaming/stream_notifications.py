class StreamNotifications:

    def live_alert(
        self,
        creator_name: str
    ):

        return f"{creator_name} is now live."


stream_notifications = StreamNotifications()