n = int(input())
#2원, 5원 으로만 거슬러준다

if n == 1:
    print(-1)
    exit()
if n == 2:
    print(1)
    exit()
if n == 3:
    print(-1)
    exit()
if n == 4:
    print(2)
    exit()
if n == 5:
    print(1)
    exit()

x = [0] * (n+1)
x[2] = 1
x[4] = 2
x[5] = 1
for i in range(6, n+1):
    if x[i-2] != 0 and x[i-5] != 0:
        x[i] = min(x[i-2], x[i-5]) + 1
    elif x[i-2] != 0:
        x[i] = x[i-2] + 1
    elif x[i-5] != 0:
        x[i] = x[i-5] + 1
    else:
        x[i] = 0

if x[n] == 0:
    print(-1)
else:
    print(x[n])