list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_ind = 0

for i in range(len(list_numbers)):
    max_num = list_numbers[max_ind]
    cur_ = list_numbers[i]
    if cur_ > max_num:
        max_ind = i

list_numbers[max_ind], list_numbers[-1] = list_numbers[-1], list_numbers[max_ind]

print(list_numbers)
