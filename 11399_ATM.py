import sys

n = int(input())
m = list(map(int, sys.stdin.readline().split()))
cnt = 0

m.sort()

for i in range(n+1):
    for j in range(i):
        cnt += m[j]

print(cnt)
