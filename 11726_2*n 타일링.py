fibo = [0] * 1001
fibo[1] = 1
fibo[2] = 2
n = int(input())
for i in range(3, n+1):
    fibo[i] = fibo[i-1]%10007 + fibo[i-2]%10007

print(fibo[n]%10007)