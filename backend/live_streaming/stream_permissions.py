class StreamPermissions:

    def can_stream(
        self,
        user_verified: bool,
        banned: bool
    ):

        if banned:
            return False

        return user_verified


stream_permissions = StreamPermissions()