import sys


t = int(input())
li = []
for i in range(t):
    li.append(int(sys.stdin.readline()))

li.sort()
for i in range(t):
    print(li[i])