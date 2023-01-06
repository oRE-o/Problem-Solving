n, k = map(int, input().split())
m = [0 for _ in range(n)]

for i in range(n):
    m[i] = int(input())

cnt = 0
for i in range(n):
    cnt += k // m[n-1-i]
    k %= m[n-1-i]

print(cnt)