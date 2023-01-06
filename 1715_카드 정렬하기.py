import sys 
import heapq

li = []
n = int(input())

for i in range(n):
    heapq.heappush(li, int(sys.stdin.readline()))

cnt = 0

if n == 1:
    print(0)
    exit()
    
while True:
    tmp = heapq.heappop(li) + heapq.heappop(li)

    if len(li) == 0:
        print(tmp+cnt)
        exit()

    cnt += tmp
    heapq.heappush(li, tmp)
