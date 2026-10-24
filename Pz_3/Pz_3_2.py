#Даны 2 целых числа A B Проверить истинность высказывания "Каждое из чисел A и B нечетное"
a = input("Введите 1 целое число ")
b = input("Введите 2 целое число ")
while not isinstance(a, int):
    try:
        a = int(a)
    except ValueError:
        print("Ошибка,неверное значение")
        a = input("Введите 1 целое число")
while not isinstance(b, int):
    try:
        b = int(b)
    except ValueError:
        print("Ошибка,неверное значение")
        b = input("Введите 2 целое число")
if a % 2 != 0 and b % 2 != 0:

    print("Условие истинно")
else:
    print("Условие ложно")
