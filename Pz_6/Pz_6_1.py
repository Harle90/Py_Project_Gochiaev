#Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
#четные числа в порядке убывания их индексов, а также их количество K.
import random
random.randint(0,100)
ListAppend = []
i = 1
while i <= 10:
    digit = random.randint(0, 100)
    i += 1
    ListAppend.append(digit)
ListAppend.sort(reverse=True)
K = len(ListAppend)
print(ListAppend)
print(K)
