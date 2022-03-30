tile = [0] * 1001
tile[1] = 1
tile[2] = 3
n = int(input())
for i in range(3, n+1):
    tile[i] = tile[i-1]%10007 + 2*tile[i-2]%10007

print(tile[n]%10007)