
class Matrix: # 정사각행렬의 곱셈이 가능한 클래스 제작
    def __init__(self, mat, ):
        self.matrix = mat
    
    def __mul__(self, other):
        a = self.matrix
        b = other.matrix
        d = len(a)
        res = [[0 for _ in range(d)] for _ in range(d)]
        for i in range(d):
            for j in range(d):
                for k in range(d):
                    res[i][j] += a[i][k] * b[k][j]
                    res[i][j] %= 1000

        newMat = Matrix(res)
        return newMat

n, b = map(int, input().split())

a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

a = Matrix(a)
E = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    E[i][i] = 1
E = Matrix(E)

def matrixPow(p, n):
    # 분할정복을 이용한 거듭제곱!
    if (n == 0):
        return E
    
    res = matrixPow(p, n//2)
    if (n % 2): # p의 지수가 홀수
        return (res * res * p)
    else: # p의 지수가 짝수
        return (res * res)

result = matrixPow(a, b).matrix
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()