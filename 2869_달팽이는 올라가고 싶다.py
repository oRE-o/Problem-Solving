a, b, v = map(int, input().split())

day = v // (a-b)
left = v % (a-b)
if left > a:
    print(day+1)
else:
    print(day+2)