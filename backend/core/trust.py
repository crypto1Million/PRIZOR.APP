def calculate_trust(user):

    score = 50

    # ✅ completed profile
    if user.profile_completion >= 80:
        score += 15

    # ✅ verified image
    if user.profile_image:
        score += 10

    # ✅ active chatting
    if user.swipes_done > 50:
        score += 10

    # ❌ reports
    score -= (user.report_count * 10)

    # ❌ warnings
    score -= (user.warning_count * 15)

    # limits
    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score