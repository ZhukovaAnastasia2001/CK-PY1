salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

total_spend = spend

for i in range (2, months + 1):
    spend = spend * (1 + increase)
    total_spend = total_spend + spend

money_capital = total_spend - salary * months

print(round(money_capital))
