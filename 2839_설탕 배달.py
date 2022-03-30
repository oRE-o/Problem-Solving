n = int(input())
# 3, 5 킬로 봉지 존재
# 최대한 적은 봉지로 n 킬로그램을 만들어라!

if n < 3 or n == 4:
    print(-1)
    exit()
elif n == 3:
    print(1)
    exit()

x = [0] * (n+2)
x[3] = 1
x[5] = 1
for i in range(6, n+1):
    if x[i-3] != 0 and x[i-5] != 0:
        x[i] = min(x[i-3], x[i-5]) + 1
    elif x[i-3] != 0:
        x[i] = x[i-3] + 1
    elif x[i-5] != 0:
        x[i] = x[i-5] + 1
    else:
        x[i] = 0

if x[n] == 0:
    print(-1)
else:
    print(x[n])