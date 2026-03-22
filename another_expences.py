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
expenses = []

def add_expence(expenses: list[float], value: float):
    add = input()
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
    print("Сумма ваших расходов: ", (get_total(expenses)))
    print("Средняя сумма расходов: ", (get_average(expenses)))
    print("-" * 30)

while choice in menu:
    if choice == "Выход":
        exit()
    if choice == "1.Добавить расход":
        add_expence(expenses, value)
    if choice == "2.Показать все расходы":
        get_total(expenses)
    if choice == "3.Показать сумму и средний расход":
        print_report(expenses)
    if choice == "4.Удалить расход по номеру":
        delete_expence(expenses, index)