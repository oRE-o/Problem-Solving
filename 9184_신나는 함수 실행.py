import sys

m = [[[-1] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    global m
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if m[a][b][c] != -1:
        return m[a][b][c]
    
    if a < b < c:
        m[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return m[a][b][c]
    
    m[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return m[a][b][c]

while(1):
    a, b, c = map(int, sys.stdin.readline().split())
    if (a == -1 and b == -1 and c == -1):
        break
    print("w(" + str(a) + ", "+str(b)+ ", "+ str(c) +") = " + str(w(a, b, c)))
    