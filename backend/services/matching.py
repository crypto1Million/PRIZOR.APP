def calculate_score(user, target):
    score = 0

    # Interest overlap
    user_interests = set(user.bio.split())
    target_interests = set(target.bio.split())
    overlap = len(user_interests & target_interests)
    score += overlap * 2

    # Age similarity
    age_diff = abs(user.age - target.age)
    if age_diff < 3:
        score += 5
    elif age_diff < 7:
        score += 2

    # Location match
    if user.location == target.location:
        score += 3

    return score