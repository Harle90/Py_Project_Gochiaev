try:
    n = int(input("Введите число N(>0) "))
    c = input("Введите значени с ")
    if n <= 0:
        print("Ошибка")
    elif len(c) != 1:
        print("Ошибка")
    else:
        res = c * n
        print("результат", res)
except ValueError:
    print("Ошибка: N должно быть целым числом.")
