print("1.Добавить расход"
      "2.Показать все расходы"
      "3.Показать сумму и средний расход"
      "4.Удалить расход по номеру"
      "5.Выход"
)
choice_user = input()

menu = ["1.Добавить расход",
        "2.Показать все расходы",
        "3.Показать сумму и средний расход",
        "4.Удалить расход по номеру",
        "5.Выход"
        ]
for choice in menu:
    if choice == "Выход":
        exit()

def add_expence(expenses: list[float], value: float):
    if value != 0:
        expenses.append(value)
    return expenses

def delete_expence(expenses: list[float], index: int):
    if 0 <= index < len(expenses):
        del expenses[index]
    return expenses

def get_total(expenses: list[float]):
    summa = sum(expenses)
    return summa

def get_average(expenses: list[float]):
    avg = sum(expenses) / len(expenses)
    return avg

def print_report(expenses: list[float]):
    print("-" * 30)
    print("Сумма ваших расходов: ", (get_total))
    print("Средняя сумма расходов: ", (get_average))
    print("-" * 30)
