import sys
m = int(sys.stdin.readline().split('\n')[0])

for i in range(m):
    s1 = []
    s2 = [] # 커서 기준으로 왼쪽 스택, 오른쪽 스택으로 나눈다
    li = sys.stdin.readline().split('\n')[0]
    for j in li: #글자마다 돌리자
        if j == '<':
            if s1: # s1의 값이 0이 아니면, 즉 맨 왼쪽이 아닌 경우
                s2.append(s1.pop()) # s1, 즉 커서 왼쪽에 있었던 문자 하나를 s2, 커서 오른쪽에 보낸다.

        elif j == '>':
            if s2:
                s1.append(s2.pop()) # 커서 오른쪽에 있던 걸 s1, 커서 왼쪽에 보낸다. 이때 s2는 역정렬 되어있음

        elif j == '-':
            if s1:
                s1.pop()
        else:
            s1.append(j)
    s1.extend(reversed(s2))
    print(''.join(s1))
