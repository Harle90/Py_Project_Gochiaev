def AddLeftDigit(d, k):
    result = int(str(d) + str(k))
    return result

K = int(input("Введите число k "))
D1 = int(input("Введите число D1 "))
D2 = int(input("Введите число D2 "))

K = AddLeftDigit(D1, K)
print(K)
K = AddLeftDigit(D2, K)
print(K)
