import re

def validate_sa_id(id_number):
    # Pattern breakdown:
    # ^\d{2}     -> Starts with 2 digits (Year)
    # (0[1-9]|1[0-2]) -> Month must be 01-09 OR 10-12
    # (0[1-9]|[12]\d|3[01]) -> Day must be 01-09, 10-29, or 30-31
    # \d{7}$     -> Ends with exactly 7 more digits
    pattern = r"^\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{7}$"
    
    if re.match(pattern, id_number):
        return True
    else:
        return False

def validate_sa_phone(phone):
    # Matches 012 345 6789 OR +2712 345 6789
    # The \s? means a space is optional
    pattern = r"^(\+27|0)\d{2}\s?\d{3}\s?\d{4}$"
    return bool(re.match(pattern, phone))

def validate_email(email):
    # Basic word@word.word
    pattern = r"^\w+@\w+\.\w+$"
    return bool(re.match(pattern, email))


def test_invalid_month():
    # This should be False because month 13 doesn't exist!
    assert validate_sa_id("9513015009087") == False 