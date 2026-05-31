class StreamRecommendations:

    def recommend(
        self,
        user_interests: list[str],
        streams: list[dict]
    ):

        results = []

        for stream in streams:

            if stream.get("category") in user_interests:
                results.append(stream)

        return results


stream_recommendations = StreamRecommendations()