t = int(input())
m = 1000000009
f = [0] * 1000001

f[1] = 1 # 0
f[2] = 2 # 11
f[3] = 4 # 111, 21, 12
 
for i in range(4, 1000001):
    f[i] = (f[i-3] + f[i-2] + f[i-1])%m

for i in range(t):
    n = int(input())
    print(f[n]%m)
