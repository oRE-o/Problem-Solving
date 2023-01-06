import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n = int(input())

visited = [[0 for _ in range(n)] for _ in range(n)]
g = [[*input().rstrip()] for _ in range(n)]
cnt = 0

def bfs_normal(a, b):
    # print(a, b)
    q = deque()

    if visited[a][b]:
        return
 
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        # print(x, y)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if g[nx][ny] == g[x][y] and not visited[nx][ny]:
                # print(f'{nx}, {ny}는 지금까지 방문 x')
                visited[nx][ny] = 1
                q.append((nx, ny))
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_normal(i, j)
            cnt += 1

print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        visited[i][j] = 0
        if g[i][j] == 'G':
            g[i][j] = 'R'

cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_normal(i, j)
            cnt += 1

print(cnt, end=' ')