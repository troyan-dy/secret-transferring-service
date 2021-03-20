import hashlib


def create_key(password, token):
    return hashlib.md5(f"{123}_{token}".encode("utf-8")).hexdigest()
