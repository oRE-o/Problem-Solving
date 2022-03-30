t = int(input())
x = [0] * 31
x[0] = 1
x[1] = 1

for i in range(2, 31):
    x[i] = x[i-1] * i

for j in range(t):
    n, m = map(int, input().split())
    # = nCr = n!/(n-r)!r!
    print(int(x[m]/(x[m-n]*x[n])))