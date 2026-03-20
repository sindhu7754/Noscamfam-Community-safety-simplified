def calculate_risk(analysis, description, incidents):
    score = 0

    # Base score from severity
    if analysis["severity"] == "high":
        score += 5
    elif analysis["severity"] == "medium":
        score += 3
    else:
        score += 1

    # Keyword boost
    if "bank" in description.lower():
        score += 2

    # Frequency boost (same type incidents)
    same_type_count = sum(
        1 for i in incidents
        if i.get("analysis", {}).get("type") == analysis["type"]
    )

    if same_type_count > 2:
        score += 2

    # Final label
    if score >= 7:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level
    }