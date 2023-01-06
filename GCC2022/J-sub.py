m = int(input())

dp = [0 for _ in range(3000)]

for i in range(3000):
    if i%m == 0:
        dp[i] = dp[i//m]
    else:
        dp[i] = dp[i//m] + 1

print(dp[0:3000])

import matplotlib.pyplot as plt

x = range(3000)
y = dp

plt.scatter(x, y)
plt.show()