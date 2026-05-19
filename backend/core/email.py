import resend

resend.api_key = "YOUR_API_KEY"


def send_verification_email(email, token):

    verification_link = (
        f"http://localhost:3000/verify/{token}"
    )

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": email,
        "subject": "Verify your account",
        "html": f"""
        <h1>Verify Your Email</h1>

        <a href="{verification_link}">
            Verify Account
        </a>
        """
    })

def send_reset_email(email, reset_link):

    print(f"Send reset link to {email}")
    print(reset_link)

def send_match_notification(email, match_username):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": email,
        "subject": "You have a new match!",
        "html": f"""
        <h1>You have a new match with {match_username}!</h1>
        <p>Start chatting now!</p>
        """
    })

    