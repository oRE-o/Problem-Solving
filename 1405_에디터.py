import sys
string = [*sys.stdin.readline().split('\n')[0]]
s1 = string
s2 = [] # 커서 기준으로 왼쪽 스택, 오른쪽 스택으로 나눈다

t = int(input())
for i in range(t):
    input() # -> 대량의 입력 받을 때 느림
    cmd = sys.stdin.readline().split('\n')[0] # -> 대량 입력시 사용, 빠른 입력
    if cmd == 'L':
        if s1: # s1의 값이 0이 아니면, 즉 맨 왼쪽이 아닌 경우
            s2.append(s1.pop()) # s1, 즉 커서 왼쪽에 있었던 문자 하나를 s2, 커서 오른쪽에 보낸다.

    elif cmd == 'D':
        if s2:
            s1.append(s2.pop()) # 커서 오른쪽에 있던 걸 s1, 커서 왼쪽에 보낸다. 이때 s2는 역정렬 되어있음

    elif cmd == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(cmd.split()[1])

s1.extend(reversed(s2))
print(''.join(s1))