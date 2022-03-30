from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
g = []
q = deque()

for i in range(h): #z
    tmp = []
    for j in range(n): #y
        tmp.append(list(map(int, sys.stdin.readline().split()))) # x
    g.append(tmp)

for z in range(h):
    for y in range(n):
        for x in range(m):
            if g[z][y][x] == 1:
                q.append((x, y, z))

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if g[nz][ny][nx] == 0:
                    g[nz][ny][nx] = g[z][y][x] + 1
                    q.append((nx, ny, nz))

bfs()
day = 0
for i in g:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)