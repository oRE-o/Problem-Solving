import sys

t = int(input())

a = []

for i in range(t):
    a.append(int(sys.stdin.readline().split()[0]))
    a.sort()
    print(a[(i+1) // 2])