def detect_vibe(profile):

    bio = (profile.bio or "").lower()

    if "gym" in bio:
        return "fitness"

    if "music" in bio:
        return "creative"

    if "anime" in bio:
        return "fandom"

    return "social"