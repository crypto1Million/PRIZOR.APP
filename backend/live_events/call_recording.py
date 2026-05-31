class CallRecording:

    def recording_allowed(
        self,
        caller_consented: bool,
        receiver_consented: bool
    ):

        return (
            caller_consented
            and receiver_consented
        )


call_recording = CallRecording()