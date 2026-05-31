class CallPermissions:

    def can_call(
        self,
        caller_id: int,
        receiver_id: int,
        matched: bool,
        blocked: bool
    ) -> bool:

        if blocked:
            return False

        if not matched:
            return False

        return True


call_permissions = CallPermissions()