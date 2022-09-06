def plus_bomb(x, y):
    mogi = a[x][y]
    for i in range(1, m+1):
        if((x-i) >= 0):
            mogi += a[x-i][y]
        if((x+i) < n):
            mogi += a[x+i][y]
        if((y-i) >= 0):
            mogi += a[x][y-i]
        if((y+i) < n):
            mogi += a[x][y+i]

    return mogi

def cross_bomb(x, y):
    mogi = a[x][y]
    for i in range(1, m+1):
        if((x-i) >= 0 and (y-i) >= 0):
            mogi += a[x-i][y-i]
        if((x-i) >= 0 and (y+i) < n):
            mogi += a[x-i][y+i]
        if((x+i) < n and (y-i) >= 0):
            mogi += a[x+i][y-i]
        if((x+i) < n and (y+i) < n):
            mogi += a[x+i][y+i]
            
    return mogi


n, m = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

maxi = 0

for i in range(n):
    for j in range(n):
        maxi = max(plus_bomb(i, j), maxi, cross_bomb(i, j))

print(maxi)