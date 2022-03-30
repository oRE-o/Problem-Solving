from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    g[a][b] = 0
    cnt = 1 #첫카운트 1로 해줘야됨
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if g[nx][ny] == 1:
                g[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1    
    return cnt


N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input())))

cnt = []
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            cnt.append(bfs(g, i, j))

cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)
