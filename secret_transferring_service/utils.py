import hashlib

KEY_SALT = 123


def create_key(password: str, token: str) -> str:
    return hashlib.md5(f"{KEY_SALT}_{token}".encode("utf-8")).hexdigest()
