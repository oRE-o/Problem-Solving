n, m = map(int, input().split())
L = list(map(int, input().split()))
A = list(map(int, input().split()))

# 정n각형이 안 되는 경우.
for i in range(n):
    while A[i] > L[i]:
        A[i] -= L[i]
        L[i] += 1

cnt = min(L)

while(1):
    if m >= L.count(min(L)):
        m -= L.count(min(L))
        cnt += 1
    else:
        break
print(L)

if cnt == 0:
    print(-1)
else:
    print(cnt)