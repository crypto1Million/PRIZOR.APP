from firebase_admin import messaging

def send_push_notification(
    token,
    title,
    body
):

    try:

        message = messaging.Message(

            notification=messaging.Notification(
                title=title,
                body=body
            ),

            token=token
        )

        response = messaging.send(message)

        return response

    except Exception as e:
        print(e)