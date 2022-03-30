n = int(input())
if n == 1:
    print(0)
    exit()
if n == 2:
    print(1)
    exit()
x = [0] * (n+1)
x[1] = 0
x[2] = 1

for i in range(3, n+1):
    x[i] = ((i-1) * (x[i-1]%1000000000 + x[i-2]%1000000000))%1000000000

print(x[n]%1000000000)