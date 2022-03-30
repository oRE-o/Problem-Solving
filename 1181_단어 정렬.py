N = int(input())

li = set()
for _ in range(N):
    li.add(input())

li = list(li)
li.sort()
li.sort(key=lambda x: len(x))
# key => sort 기준.
for i in li:
    print(i)