b = [0, 0, 0, 0, 0, 0, 0, 0, 0]

big = 0
wichi = 0

for i in range(9):
    b[i] = int(input())

    if b[i] > big:
        big = b[i]
        wichi = i+1

print(big)
print(wichi)
        