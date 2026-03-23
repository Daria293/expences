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

while choice != menu[4]:
    choice = int(input())
    if  choice == 1:
        value = input()
        print(add_expence(expenses, value))
    elif choice == 2:
        print(list[expenses])
    elif choice == 3:
        print_report(expenses)
    elif choice == 4:
        index = input()
        print(delete_expence(expenses, index))