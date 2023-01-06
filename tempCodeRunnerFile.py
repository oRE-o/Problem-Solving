import sys 
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

visited = [[0 for _ in range(n)] for _ in range(n)]
g = []
cnt = 0

for _ in range(n):
    g.append(sys.stdin.readline().rstrip())

# print(g)

def bfs_RGblind(a, b):
    global cnt, g
    q = deque()

    if visited[a][b]:
        return

    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if g[nx][ny] == g[x][y] \
                    or ( g[nx][ny] == 'R' and g[x][y] == 'G') \
                    or (g[nx][ny] == 'G' and g[x][y] == 'R'):
                    if not visited[nx][ny]:
                        q.append((nx, ny))
    cnt += 1


def bfs_normal(a, b):
    global cnt, g
    q = deque()

    if visited[a][b]:
        return

    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if g[nx][ny] == g[x][y]:
                    if not visited[nx][ny]:
                        q.append((nx, ny))
    cnt += 1


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_normal(i, j)

print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        visited[i][j] = 0

cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_RGblind(i, j)

print(cnt, end=' ')