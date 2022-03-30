
import sys
t = int(sys.stdin.readline())
# 빠른 입출력 사용해야함. 입력값이 많기 때문이다.

queue = [0] * t
first = 0
last = -1

for i in range(t): #단순 반복
    command = sys.stdin.readline().split('\n')[0]
    # print("command: ", command)
    if command == 'pop':
        if last < first:
            print(-1)
        else:
            print(queue[first])
            queue[first] = 0
            first += 1
            
    if command == 'size':
        print(last-first+1)

    if command == 'empty':
        if last < first:
            print(1)
        else:
            print(0)

    if command == 'front':
        if last < first:
            print(-1)
        else:
            print(queue[first])

    if command == 'back':
        if last < first:
            print(-1)
        else:
            print(queue[last])

    if command[0:4] == 'push':
        last += 1
        queue[last] = int(command.split()[1])
        
    # print("Now Queue : ", queue, "|| first :", first, ", last :",last)
