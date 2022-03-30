from collections import deque

m, n = map(int, input().split())
g = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

g = [list(map(int, input().split())) for _ in range(n)]

q = deque(())

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            q.append((j, i))

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if g[ny][nx] == 0:
                    g[ny][nx] = g[y][x] + 1
                    q.append((nx, ny))

bfs()
res = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(-1)
            exit()
    res = max(res, max(g[i]))

print(res - 1)