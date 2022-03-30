from collections import deque
import sys

n = int(input())
t = int(input())

g = [[0 for _ in range(101)] for _ in range(101)] 
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    g[a][b] = 1
    g[b][a] = 1

q = deque()
q.append(1)
visited = [0] * 101

while q:
    v = q.popleft()
    visited[v] = 1
    for i in range(1, n+1):
        if g[v][i] == 1 and visited[i] == 0:
            q.append(i)

print(visited.count(1)-1)
