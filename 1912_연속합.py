import sys

n = int(input())
a = list(map(int, input().split()))

cache = [0] * n
cache[0] = a[0]

for i in range(1, n):
    cache[i] = max(a[i], cache[i-1]+a[i])

print(max(cache))