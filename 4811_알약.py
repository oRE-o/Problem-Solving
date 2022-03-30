
t = [0] * 31

t[0] = 1
t[1] = 1

for i in range(2, 31): # i 번째를 구하기 위함
    for j in range(0, i):  # 0 ~ n-1 더하기 위함
        t[i] += t[j] * t[i-j-1]

n = 1
while(1):
    n = int(input())
    if(n == 0):
        exit()
    print(t[n])
