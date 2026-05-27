def generate_match_insight(user1, user2):

    insights = []

    user1_bio = (user1.bio or "").lower()
    user2_bio = (user2.bio or "").lower()

    if "gym" in user1_bio and "gym" in user2_bio:
        insights.append(
            "You both share strong fitness energy and active lifestyles."
        )

    if "music" in user1_bio and "music" in user2_bio:
        insights.append(
            "Music seems important to both of your personalities."
        )

    if "fashion" in user1_bio and "fashion" in user2_bio:
        insights.append(
            "You both express strong fashion and aesthetic interests."
        )

    if "travel" in user1_bio and "travel" in user2_bio:
        insights.append(
            "Both of you appear adventurous and socially explorative."
        )

    if not insights:

        insights.append(
            "You both seem socially compatible based on your profile energy."
        )

    return insights

def calculate_compatibility_score(user1, user2):

    score = 50

    user1_bio = (user1.bio or "").lower()
    user2_bio = (user2.bio or "").lower()

    keywords = [
        "gym",
        "music",
        "fashion",
        "travel",
        "anime",
        "gaming",
        "art",
        "crypto",
        "fitness",
        "social",
        "dancing"
    ]

    for keyword in keywords:

        if keyword in user1_bio and keyword in user2_bio:
            score += 7

    return min(score, 95)    