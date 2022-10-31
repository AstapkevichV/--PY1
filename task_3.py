def delete(list_, index=None):
    if index is not None:  # TODO реализовать функцию удаления элемента из списка по индексу
        a = list_[:index]
        b = list_[index+1:]
        final = a + b
        return final
    else:
        index = -1
        return list_[:index]

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
