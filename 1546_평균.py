a = int(input())
b = list(range(a))
maxi = 0
sum = 0

b = list(map(int,input().split()))
maxi = max(b)

for i in range(a):
    sum = sum + b[i] / maxi * 100

print(sum / a)