n = int(input())
m = 1000-n
money = [500, 100, 50, 10, 5, 1]
sum = 0

for cash in money:
    sum += (m // cash)
    m %= cash

print(sum)