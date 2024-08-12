def not_less_then_8_chars(s: str):
    """не менше 8 символів"""
    return len(s) >= 8


def one_big_one_small(s: str):
    """має бути 1 велика та 1 мала літера"""
    lower = False
    upper = False

    for char in s:
        if char.isupper():
            upper = True

        if char.islower():
            lower = True

    return lower and upper


def number_in_password(s: str):
    """має бути цифра"""
    for char in s:
        if char.isdigit():
            return True

    return False


def symbol_in_password(s: str):
    """має бути символ"""
    for char in s:
        if not char.isalnum():
            return True

    return False


descriptions = {
    0: "very bad",
    1: "bad",
    2: "weak",
    3: "good",
    4: "very good",
}


def check_pswd(password):
    points = 0

    if not_less_then_8_chars(password):
        points += 1

    if one_big_one_small(password):
        points += 1

    if number_in_password(password):
        points += 1

    if symbol_in_password(password):
        points += 1

    return descriptions[points]
