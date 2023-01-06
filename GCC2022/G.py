import math, sys
T = int(input())

for _ in range(T):
    n, a, b = map(int, sys.stdin.readline().rstrip().split())
    r = math.sqrt(b/math.pi)
    x = math.sqrt(2*a/(n*math.sin(2*math.pi/n)))
    t = 2*math.sqrt(math.tan(math.pi/n)*a/n)

    cnt = 1

    if r >= x:
        print(n)
        continue

    for i in range(math.floor(n/2)):
        l = t * math.sin(math.pi*(i+1)/n) / math.sin(math.pi/n)
        
        if (l > 2*r):
            print(i+1)
            break
    
            