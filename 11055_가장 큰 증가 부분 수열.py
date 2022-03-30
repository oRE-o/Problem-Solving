input()
a = list(map(int, input().split()))
cache = [0] * (len(a)+1)
for i in range(len(a)): # a[0] ~ a[len(a)-1]
    cache[i] = a[i]
    for j in range(i): # 차례로 비교하기 위한 반복문.
        if a[i] > a[j]: # i번째 구하기 : 뒤부터 하나씩 검사, i번째가 더 크다면
            cache[i] = max(cache[i], cache[j] + a[i]) # 현 캐시와 증가 시 캐시 + 자기자신의 값을 비교하여 큰걸 책정.

print(max(cache))