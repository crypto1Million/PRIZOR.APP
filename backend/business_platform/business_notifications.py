class BusinessNotifications:

    def notify(
        self,
        message: str
    ):

        return {
            "sent": True,
            "message": message
        }


business_notifications = BusinessNotifications()