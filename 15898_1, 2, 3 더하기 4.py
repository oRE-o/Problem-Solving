import sys
t = int(input())

f = [[0 for _ in range(3)] for _ in range(10001)]
f[1][0] = 1
f[2][0] = 1
f[2][1] = 1
f[3][0] = 1
f[3][1] = 1
f[3][2] = 1

for i in range(4, 10001):
    # 점화식 작성 시, 중복경우를 없애는 방법으로 "오름차순" 을 택한다고 보면 된다.
    # 오름차순으로 정렬한다면, 새로이 더해지는 값이 2면 그 전 숫자는 1, 2만 올 수 있으므로..!
    f[i][0] = f[i-1][0]
    f[i][1] = f[i-2][1] + f[i-2][0]
    f[i][2] = f[i-3][2] + f[i-3][1] + f[i-3][0]

for i in range(t):
    n = int(sys.stdin.readline())
    print(f[n][0] + f[n][1] + f[n][2])