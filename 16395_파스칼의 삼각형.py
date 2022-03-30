from math import factorial
n, k = map(int, input().split())
result = factorial(n-1) // (factorial(k-1) * factorial(n - k))
print(result)