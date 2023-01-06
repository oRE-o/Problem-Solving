import sys
import math
T = int(input())

# k 는 0부터 정수

for _ in range(T):
    a, b, m, n = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0

    # n*m ~ n*m+n 까지 a, b 사이 갯수?    
    for i in range((n-1)*m+1, n*m+1):
        if (a <= i <= b):
            cnt += 1

    print(cnt)