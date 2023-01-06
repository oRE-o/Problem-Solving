import sys
n = int(input())

ans = 0
a, b = map(int, sys.stdin.readline().split())
for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    if x > a and y < b:
        continue

    if x <= b and y >= a: # 겹침
        b = y
    elif x <= b and y > a:
        continue
    elif x > b: # 선분이 분리됨
        ans += (b - a)
        a = x
        b = y
    
ans += (b - a)
print(ans)