try:
    kg, cm = map(int , input("Введите сначала вес,потом рост: ").split())
    print(kg / (cm / 100) ** 2)
except ValueError:
    print("Ошибка! Вы ввели не число!")