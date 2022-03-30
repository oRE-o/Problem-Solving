n = int(input())

if n == 1 or n == 2:
    print(1)
    exit()
f = [0] * (n+1)

f[1] = 1
f[2] = 1

for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]

print(f[n])