class StreamModeration:

    banned_words = [
        "spam",
        "scam",
        "abuse"
    ]

    def is_allowed(
        self,
        message: str
    ):

        text = message.lower()

        for word in self.banned_words:

            if word in text:
                return False

        return True


stream_moderation = StreamModeration()