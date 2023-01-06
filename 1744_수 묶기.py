import sys

plus = []
zero = []
minus = []
ans = 0

n = int(input())
for i in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        plus.append(a)
    elif a == 0:
        zero.append(a)
    else:
        minus.append(a)

plus.sort()
minus.sort(reverse=True)

while len(plus) != 0:
    if len(plus) == 1:
        ans += plus.pop()
    else:
        a = plus.pop()
        b = plus.pop()
        if (a*b) > (a+b):
            ans += a*b
        else:
            ans += (a+b)

while len(minus) != 0:
    if len(minus) == 1:
        if len(zero) != 0:
            ans += 0
            zero.pop()
            minus.pop()
        else:
            ans += minus.pop()
    else:
        ans += minus.pop() * minus.pop()

print(ans)