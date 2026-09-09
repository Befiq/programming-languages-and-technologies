try:
    a, b = map(int, input(). split())
    print("Сумма :",a + b,"\n","Разность :",a - b,"\n","Произведение :",a * b,"\n","Частное:",a // b)
except ValueError:
    print("Ошибка! Вы ввели не число!")