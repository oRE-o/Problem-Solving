t = int(input())
m = 1000000009

f_odd = [0] * 100001
f_even = [0] * 100001

f_odd[1] = 1
f_even[1] = 0

f_odd[2] = 1
f_even[2] = 1

f_odd[3] = 2
f_even[3] = 2

for i in range(4, 100001):
    f_odd[i] = f_even[i-1]%m + f_even[i-2]%m + f_even[i-3]%m
    f_even[i] = f_odd[i-1]%m + f_odd[i-2]%m + f_odd[i-3]%m

for i in range(t):
    n = int(input())
    print(f_odd[n]%m, f_even[n]%m)
