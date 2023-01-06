p = 1000000007


def multi(a, b):
    temp = [[0 for _ in range(len(b[0]))] for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k]*b[k][j]
            temp[i][j] = sum % p
    return temp

def power(a, n):
    if n == 1:
        return a
    elif n % 2:
        return multi(power(a, n-1), a)
    else:
        return power(multi(a, a), n//2)

adj=[[1, 1], [1, 0]]
start = [[1], [1]]

n = int(input())

if n < 3:
    print(1)

else:
    print(multi(power(adj, n-2), start)[0][0])
