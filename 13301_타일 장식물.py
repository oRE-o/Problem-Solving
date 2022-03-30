n = int(input())
if n == 1:
    print(4)
    exit()

if n == 2:
    print(6)
    exit()

if n == 3:
    print(10)
    exit()

x = [0] * 81
x[1] = 1
x[2] = 1

for i in range(3, n+1):
    x[i] = x[i-1] + x[i-2]

print(x[n]*4 + x[n-1]*2)