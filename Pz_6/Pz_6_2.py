a = [1, 3, 5, 2, 4, 4, 7, 9]  # пример списка размера N

count = 0
growing = False

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        if not growing:
            count += 1
            growing = True
    else:
        growing = False

print("Количество возрастающих участков:", count)
