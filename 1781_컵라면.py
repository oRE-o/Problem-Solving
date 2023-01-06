import heapq, sys
N = int(input())
li = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    li.append((a, b))

li.sort()

queue = []

for i in li:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))

