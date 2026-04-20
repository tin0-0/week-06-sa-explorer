from password_strength import check_strength


def test_short_password_is_weak():
    assert check_strength("abc") == "weak"


def test_long_password_width_digit_is_strong():
    assert check_strength("HelloWorld123") == "strong"


def test_long_password_no_digit_is_meduim():
    assert check_strength("HelloWorld") == "medium"
