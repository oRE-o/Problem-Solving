
a, b, c = map(int, input().split())
mod = c

def fpow(a, n):
    if (n == 0):
        return  1
    res = fpow(a, n//2)
    if (n % 2):
        return (res * res * a) % mod
    else:
        return (res * res) % mod

print(fpow(a, b))