expences = str((input("Введите сумму трат: ")).lower())
if "руб" not in expences:
    print("Неверный формат суммы")
elif "коп" not in expences:
    rub8, rub9 = expences.split(" ")
    if len(rub8) >= 1 and rub8.isdigit():
        print(f"{float(rub8):.2f} ₽")
    else:
        print("Неверный формат суммы")
else:
    rub, rub1, kop, kop1 = expences.split(" ")
    if len(rub) == 0:
        print("Неверный формат суммы")
    elif not rub.isdigit():
        print("Неверный формат суммы")
    elif len(kop) == 0 and len(kop1) == 0:
        print(f"{rub:.2f}, ₽")
    else:
        print(f"{rub}.{kop:02} ₽")
