import sys
t = int(sys.stdin.readline())
# 빠른 입출력 사용해야함. 입력값이 많기 때문이다.

stack = [0] * t
top = -1

for i in range(t): #단순 반복
    command = sys.stdin.readline().split('\n')[0]
    if command == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            stack[top] = 0
            top -= 1
            
    if command == 'size':
        print(top+1)
    if command == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    if command == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    if command[0:4] == 'push':
        top += 1
        stack[top] = int(command.split()[1])