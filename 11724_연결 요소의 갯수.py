from collections import deque

n, m = map(int, input().split())
g = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1

visited = [0 for _ in range(n+1)]
components = 0

def bfs(g, v):
    q = deque()
    visited[v] = 1
    q.append(v)

    while q:
        x = q.popleft()
        for i in range(1, n+1):
            if g[x][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1


for i in range(1, n+1):
    if visited[i] == 0:
        bfs(g, i)
        components += 1

print(components)