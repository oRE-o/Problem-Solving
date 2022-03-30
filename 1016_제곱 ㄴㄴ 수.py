min, max = map(int, input().split())
li = [1]*(max - min + 1) # 일단 모두 다 제곱 ㄴㄴ수라고 본다.

for i in range(2, int(max ** 0.5) + 1): # 제곱수 t 설정
    t = i**2
    for j in range(min//t*t, max+1, t): # (min를 t로 나눈 몫)*t부터 최대까지 i제곱으로 건너뛰면서 색칠 (min 전에 있는 거부터 색칠하는거)
        if j - min >= 0 and li[j - min]: # j가 min이나 그보다 크고, li[j-min] 이 1이면 바꿔먹는다
            li[j - min] = 0 # j-min 을 0으로 설정
print(li.count(1))