import sys


while(1):
    li = list(map(int, sys.stdin.readline().split()))
    if li[0] == li[1] == li[2] == 0:
        break
    
    c = max(li)
    li.remove(c)

    if c**2 == li[0] ** 2 + li[1] ** 2:
        print("right")
    else:
        print('wrong')