BANNED_WORDS = [
    "scam",
    "bitcoin doubler",
    "onlyfans leak",
    "nude",
    "sex",
    "porn",
    "telegram link",
    "onlyfans",
]  


def contains_banned_content(text):

    text = text.lower()

    for word in BANNED_WORDS:

        if word in text:
            return True

    return False