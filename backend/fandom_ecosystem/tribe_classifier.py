# backend/fandom_ecosystem/tribe_classifier.py

class TribeClassifier:

    FANDOM_TYPES = [

        "drag",
        "queer_anime",
        "kpop",
        "queer_gaming",
        "ballroom",
        "fashion",
        "alt_music",
        "cosplay",
        "streetwear",
        "rupaul",
        "webtoon",
        "visual_novels",
        "indie_music",
        "queer_cinema",
    ]

    def classify(self, user_profile: dict):

        interests = user_profile.get("interests", [])

        for fandom in self.FANDOM_TYPES:

            if fandom in interests:
                return fandom

        return "general_community"