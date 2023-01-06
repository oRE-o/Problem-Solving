a, b = map(int, input().split())

cnt = 1

while b != a:
    if b < a:
        print(-1)
        exit()

    if b % 2 == 0:
        b //= 2
        cnt += 1
        
    elif b % 10 == 1:
        b //= 10 # 마지막 1 빼고 다 가져오기
        cnt += 1

    else:
        print(-1)
        exit()

print(cnt)