import sys
t = int(input())

f = [0] * 10001
f[1] = 1
f[2] = 1

for j in range(3, 10001):
    f[j] = f[j-1] + f[j-2]

for i in range(t):
    p, q = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {f[p]%q}")
