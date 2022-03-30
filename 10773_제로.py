
k = int(input())
a = []
sum = 0
for i in range(k):
    cmd = int(input())
    if cmd == 0:
        a.pop()
    else:
        a.append(cmd)

for i in a:
    sum += i

print(sum)