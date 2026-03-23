print("1.Добавить расход"
      "2.Показать все расходы"
      "3.Показать сумму и средний расход"
      "4.Удалить расход по номеру"
      "5.Выход"
)


menu = ["1.Добавить расход",
        "2.Показать все расходы",
        "3.Показать сумму и средний расход",
        "4.Удалить расход по номеру",
        "5.Выход"
        ]
expenses = []

def add_expence(expenses: list[float], value: float):
    
    if float(value) != 0:
        expenses.append(value)
    return list[expenses]

def delete_expence(expenses: list[float], index: int):
    if 0 <= int(index) < len(expenses):
        del expenses[index]
    return expenses

def get_total(expenses: list[float]):
    summa = sum(expenses)
    return summa

def get_average(expenses: list[float]):
    if len(expenses) == 0:
        print("Ошибка")
    else:
        avg = sum(expenses) / len(expenses)
    return avg

def print_report(expenses: list[float]):
    print("-" * 30)
    print("Сумма ваших расходов: ", (get_total(expenses)))
    print("Средняя сумма расходов: ", (get_average(expenses)))
    print("-" * 30)
choice = input()
while choice in menu:
    if choice == menu[4]:
        exit()
    if choice == menu[0]:
        value = input()
        add_expence(expenses, value)
    if choice == menu[1]:
        list[expenses]
    if choice == menu[2]:
        print_report(expenses)
    if choice == menu[3]:
        index = input()
        delete_expence(expenses, index)