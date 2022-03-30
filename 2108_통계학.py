from collections import Counter
import sys

n = int(input())
li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort()
print(int(round(sum(li)/n, 0)))
print(li[n//2])

c = Counter(li).most_common()
if len(c) > 1 and c[0][1]==c[1][1]: # 카운터에서 두개 존재한다면 다음껄 출력해줘야함
    print(c[1][0])
else:
    print(c[0][0])

print(max(li)-min(li))
