import random
import string

chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)


def get_random_password(length) -> str:
    password = []
    for _ in range(length):
        password = random.sample(chars, length)
        ''.join(password)
    return ''.join(password)


print(get_random_password(8))
# _
