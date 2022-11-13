import string
from random import sample


def get_random_password() -> str:
    n = 8
    symbol = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
    return ''.join(sample(symbol, n))


print(get_random_password())
