#Еденицы ихмерения пронумерованы следующим образом 1 - децеметр 2 километр 3 метр 4 миллиметр 5 сантиметр Дан номер еденицы длины (целое число в диапазоне 1-5)
#и длина отрезка в этих еденицах (вещественное число) Найти длину отрезка в метрах
a = input("Введите еденицу измерения")
b = input("Введите длину отрезка")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неверные данные,попробуйте снова")
        a = input("Введите еденицу измерения")
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print('Неверные данные,попробуйте снова')
        b = input("Введите еденицу измерения")
else:
        if a == 1:
            meters = b * 0.1
        elif a == 2:
            meters = b * 1000
        elif a == 3:
            meters = b
        elif a == 4:
            meters = b * 0.001
        elif a == 5:
            meters = b * 0.01
        else:
            meters = None
            print("Ошибка, диапозон должен быть от 1-5")
        if meters != None:
            print(meters)
