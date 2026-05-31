class StreamGifts:

    def send_gift(
        self,
        sender_id: int,
        receiver_id: int,
        gift_name: str,
        value: float
    ):

        return {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "gift_name": gift_name,
            "value": value
        }


stream_gifts = StreamGifts()