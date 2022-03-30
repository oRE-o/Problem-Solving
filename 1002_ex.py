import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    if d < r1+r2:
        print(2)
    elif d == r1+r2:
        print(1)
    else:
        print(0)