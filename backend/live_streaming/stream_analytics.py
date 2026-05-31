class StreamAnalytics:

    def metrics(
        self,
        viewers: int,
        likes: int,
        messages: int
    ):

        return {
            "viewers": viewers,
            "likes": likes,
            "messages": messages
        }


stream_analytics = StreamAnalytics()