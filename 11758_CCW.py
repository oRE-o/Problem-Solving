import sys

p = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
if (p[1][0] - p[0][0]) * (p[2][1] - p[0][1]) > (p[1][1] - p[0][1]) * (p[2][0] - p[0][0]):
    print(1)
elif (p[1][0] - p[0][0]) * (p[2][1] - p[0][1]) < (p[1][1] - p[0][1]) * (p[2][0] - p[0][0]):
    print(-1)
else:
    print(0)