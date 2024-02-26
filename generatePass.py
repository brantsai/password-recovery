import secrets


def generate_pass():
    password_length = 13
    return secrets.token_urlsafe(password_length)
