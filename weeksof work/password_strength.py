def check_strength(password):
    if len(password) >= 8 and any(c.isdigit() for c in password):
        return "strong"

    return "weak"
