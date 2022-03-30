k = int(input())
a = [0] * 46
b = [0] * 46

a[1] = 0
b[1] = 1


for i in range(2, k+1):
    a[i] = b[i-1]
    b[i] = b[i-1] + a[i-1]

print(a[k], b[k], end=' ')