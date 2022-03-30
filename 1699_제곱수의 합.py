import sys
 
input = sys.stdin.readline

sum = [i for i in range(100001)]

n = int(input())
for i in range(1, n+1):
    for j in range(1, i): 
        if j*j > i:
            break
        if sum[i] > sum[i-j*j] + 1: 
            sum[i] = sum[i-j*j] + 1
        
print(sum[n])