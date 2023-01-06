n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

cnt = 0
for i in range(n):
    cnt += a[i] * b[i]

print(cnt)