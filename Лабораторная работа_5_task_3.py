import random
from random import randint


def get_unique_list_numbers() -> list[int]:
    set_ = set()
    while len(set_) < 15:
        set_.add(randint(-10, 10))
    list_ = list(set_)
    random.shuffle(list_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# _
