from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(g, a, b):
    q = deque()
    q.append((a, b))
    g[a][b] = 0
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if g[nx][ny] == 1:
                    g[nx][ny] = 0
                    q.append((nx, ny))

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())

    g = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        g[x][y] = 1

    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                bfs(g, i, j)
                cnt += 1
    print(cnt)
