a = [2, 4, 6, 8]
res = []
for i in range(len(a)):
    if i == 0:
        s = a[0] + a[1]
        res.append(s/2)
    elif i == len(a) - 1:
        s = a[-2] + a[-1]
        res.append(s/2)
    else:
        s = a[i-1] + a[i] + a[i+1]
        res.append(s/3)
print(res)
print(a)
