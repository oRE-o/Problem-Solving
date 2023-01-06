import sys

n, k = map(int, input().split())
li = [0 for _ in range(n)]
dp = [0 for _ in range(k+1)]
for i in range(n):
    li[i] = int(sys.stdin.readline())

dp[0] = 1

for i in li:
    for j in range(i, k+1):
        if j>= i and dp[j - i]:
            dp[j] += dp[j - i] 

print(dp)
print(dp[k])