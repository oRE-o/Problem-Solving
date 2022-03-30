a = list(range(10))
cnt = 1
for i in range(10):
    a[i]= int(input())%42

a.sort()

for i in range(9):
    if a[i]!= a[i+1]:
        cnt+=1

print(cnt)