from random import randint


def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count = 15

    random_digits = []
    seen = set()
    for i in range(count):
        x = randint(start, stop)
        while x in seen:
            x = randint(start, stop)
        seen.add(x)
        random_digits.append(x)
    return random_digits

    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
