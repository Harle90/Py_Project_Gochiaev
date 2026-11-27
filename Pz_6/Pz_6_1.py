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
