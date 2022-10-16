salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

cur_spend = spend
for cur_capital in range(1, months + 1):
    cur_capital = (cur_spend - salary)
    cur_spend = cur_spend * (increase + 1)
    need_money += cur_capital

print(round(need_money))
