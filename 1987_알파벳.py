from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
g = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = set()
    q.add((0, 0, g[0][0]))
    cnt = 1

    #BackTracking을 하기 위해서는 각 경우의 수마다, 번째마다 나온 알파벳을 각각의 배열에 담아야..
    while q:
        x, y, string = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R:
                if g[ny][nx] not in string:
                    q.add((nx, ny, string + g[ny][nx]))
                    cnt = max(cnt, len(string)+1)
    return cnt

print(bfs())
