n = int(input())
a = []
numlist = []
alphadict = {}

for i in range(n):
    a.append(input())
    for j in range(len(a[i])):
        if a[i][j] in alphadict:
            alphadict[a[i][j]] += 10 ** (len(a[i]) - j - 1)
        else:
            alphadict[a[i][j]] = 10 ** (len(a[i]) - j - 1)

for val in alphadict.values():
    numlist.append(val)

numlist.sort(reverse=True)

cnt = 0
number = 9

for i in numlist:
    cnt += number * i
    number -= 1

print(cnt)