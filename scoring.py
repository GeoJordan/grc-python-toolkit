def score_control(row):
    score = 0

    if row.get("hipaa_match"):
        score += 2

    if "encryption" in str(row.get("discussion", "")).lower():
        score += 2

    if "access control" in str(row.get("discussion", "")).lower():
        score += 2

    return score


def assign_risk(score):
    if score >= 4:
        return "Low Risk"
    elif score >= 2:
        return "Moderate Risk"
    return "High Risk"

