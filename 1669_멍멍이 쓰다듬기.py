x, y = map(int, input().split())
dist = y - x
cnt = 0 # 이동거리
n = 0 # 횟수

while (dist > cnt):
    cnt += n // 2 + 1
    n += 1

print(n)