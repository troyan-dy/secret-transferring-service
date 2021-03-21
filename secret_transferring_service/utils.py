import hashlib


def create_key(password: str, token: str) -> str:
    return hashlib.md5(f"{123}_{token}".encode("utf-8")).hexdigest()
