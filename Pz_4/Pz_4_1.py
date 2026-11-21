#Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A до B включительно.
try:
    a = int(input("Введите 1 число "))
    b = int(input("Введите 2 число "))

except ValueError:
    print("Ошибка, неверные значения")
else:
    summ = 0
    while a <= b:
        summ += a ** 2
        a += 1
    print(f"Сумма квадратов{summ}")
