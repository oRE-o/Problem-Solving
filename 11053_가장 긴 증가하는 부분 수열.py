input()
a = list(map(int, input().split()))
cache = [0] * (len(a)+1)
for i in range(len(a)): # a[0] ~ a[len(a)-1]
    cache[i] = 1
    for j in range(i):
        if a[i] > a[j]:
            cache[i] = max(cache[i], cache[j] + 1)

print(max(cache))