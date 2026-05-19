from datetime import datetime


def calculate_discovery_score(user):

    like_ratio = min(user.like_ratio or 0, 1)
    activity_score = min(user.activity_score or 0, 1)

    elo_score = min((user.elo_score or 0) / 1000, 2)

    exposure_penalty = max(
        user.exposure_penalty or 1,
        0.2
    )

    match_boost = user.match_boost or 1
    boost = user.boost_multiplier or 1

    score = (
        (like_ratio * 0.3) +
        (activity_score * 0.2) +
        (elo_score * 0.5)
    )

    return score * exposure_penalty * match_boost * boost