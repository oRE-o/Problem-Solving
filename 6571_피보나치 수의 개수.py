fibo = [0] * 10001
fibo[1] = 1
fibo[2] = 2

for i in range(3, 10001):
    fibo[i] = fibo[i-1] + fibo[i-2]

while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    cnt = 0
    for j in range(1, 10001):
        if a <= fibo[j] and fibo[j] <= b:
            cnt += 1
            if fibo[j] > b:
                break

    print(cnt)