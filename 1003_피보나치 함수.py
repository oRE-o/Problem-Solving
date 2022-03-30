t = int(input())
zero = [0] * 41
one = [0] * 41
zero[0] = 1
one[1] = 1
for i in range(t):
    n = int(input())
    for j in range(2, n+1):
        zero[j] = zero[j-1] + zero[j-2]
        one[j] = one[j-1] + one[j-2]

    print(zero[n], one[n])

# 0 -> 1, 0
# 1 -> 0, 1
# 2 -> 1+0 , 0+1
# 3 -> 0+1 , 