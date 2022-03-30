a, b = map(int, input().split())
fibo = [0] * b+4
fibo[0] = 0
fibo[1] = 1
for i in range(2, b+3):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[b+2]- fibo[a+1])