fibo = [0] * 1000001
fibo[0] = 0
fibo[1] = 1
n = int(input())
for i in range(2, n+1):
    fibo[i] = fibo[i-1]%1000000007 + fibo[i-2]%1000000007

print(fibo[n]%1000000007)