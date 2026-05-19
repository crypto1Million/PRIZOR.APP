import requests

API_USER = "YOUR_API_USER"
API_SECRET = "YOUR_API_SECRET"


def check_image_safe(image_url):

    response = requests.get(
        "https://api.sightengine.com/1.0/check.json",
        params={
            'url': image_url,
            'models': 'nudity-2.1,weapon,recreational_drug,gore',
            'api_user': API_USER,
            'api_secret': API_SECRET
        }
    )

    result = response.json()

    nudity = result["nudity"]

    if nudity["sexual_activity"] > 0.5:
        return False

    if nudity["sexual_display"] > 0.5:
        return False

    return True

def moderate_image(image_path):

    return True    