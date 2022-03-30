n = int(input())
f = [0] * 1000001
f[1] = 1
f[2] = 2

for i in range(3, n+1):
    f[i] = f[i-1]%15746 + f[i-2]%15746

print(f[n]%15746)