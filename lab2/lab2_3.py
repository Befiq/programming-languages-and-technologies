try:
    Vklad, proc, god = map(int, input("Введите сумму,процент,кол-во лет: ").split())
    print(Vklad * (1 + proc / 100) ** god)
except ValueError:
    print("Ошибка! Вы ввели не число!")