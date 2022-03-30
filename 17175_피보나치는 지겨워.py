fibocnt = [0] * 51
fibocnt[0] = 1
fibocnt[1] = 1
n = int(input())
for i in range(2, n+1):
    fibocnt[i] = 1 + fibocnt[i-1]%1000000007 + fibocnt[i-2]%1000000007

print(fibocnt[n]%1000000007)