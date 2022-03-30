n, m = map(int, input().split())
f = [0] * 101
f[0] = 1
f[1] = 1

for i in range(2, n+1):
    f[i] = f[i-1] * i

print(f[n] // (f[n-m] * f[m]))