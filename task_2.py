def get_count_char(str_):
    dict_ = {}  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = ''.join(str_.lower().split())
    for charts in str_:
        if charts.isalpha():
            if charts in dict_:
                dict_[charts] += 1
            else:
                dict_[charts] = 1

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def get_count_perc(perc_):

    for a, b in perc_.items():
        n = round(int(b) / sum(perc_.values()) * 100, 2)
        perc_[a] = n

    return perc_


print(get_count_perc(get_count_char(main_str)))
