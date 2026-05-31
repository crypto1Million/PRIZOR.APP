import secrets


class RTCTokenService:

    def generate_token(
        self,
        user_id: int
    ):

        return {
            "user_id": user_id,
            "token": secrets.token_urlsafe(32)
        }


rtc_token_service = RTCTokenService()