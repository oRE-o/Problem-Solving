a = int(input())
if a > 0:
    print(1)

elif a == 0:
    print(0)

else:
    if a%2 == 0:
        print(-1)
    else:
        print(1)
        
a = abs(a)
fibo = [0] * 1000001
fibo[0] = 0
fibo[1] = 1
for i in range(2, a+1):
    fibo[i] = fibo[i-1]%1000000000 + fibo[i-2]%1000000000

print(fibo[a]%1000000000)

# 1:1 0:0 -1:1 -2:-1 -3:2