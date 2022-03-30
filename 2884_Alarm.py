h, m = map(int, input().split())

if m >= 45:
    m = m-45
else :
    if h == 0:
        h = 23
    else:
        h = h - 1
    m = m + 15

print(h, m)