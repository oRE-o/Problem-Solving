from collections import deque

n = int(input())
g = []
visited = [0] * n
for i in range(n):
    g.append(list(map(int, input().split())))

for k in range(0, n) :
    for i in range(0, n) :
        for j in range(0, n):
            if g[i][k] and g[k][j] :
                g[i][j] = 1
                
for i in range(n):
    for j in range(n):
        print(g[i][j], end=' ')
    print()