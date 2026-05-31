class StreamDiscovery:

    def trending_score(
        self,
        viewers: int,
        engagement: int
    ):

        return viewers + engagement


stream_discovery = StreamDiscovery()