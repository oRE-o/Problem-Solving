a = int(input())
b = list(map(int, input().split()))

big = -1000000
small = 1000000

for i in range(a):
    if big < b[i]:
        big = b[i]

    if small > b[i]:
        small = b[i]

print(small, big)