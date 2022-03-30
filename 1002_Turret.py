T = input()

for i in range(int(T)):
    xj, yj, rj, xb, yb, rb = map(float, input().split())
    
    d = ((xb - xj) ** 2 +(yb - yj) **2 ) **0.5
    
    if(xj == xb and yj == yb): # 중심 동일
        if(rj == rb):
            print(-1)
        elif(rj != rb):
            print(0)
            

    if(d != 0 and d < max(rb, rj)): # 내접
        if d == abs(rb-rj):
            print(1)
        elif d > abs(rb-rj):
            print(2)
        elif d < abs(rb-rj):
            print(0)


    if(d >= max(rb, rj)):
        if(d < rb+rj):
            print(2)
        elif(d == rb+rj):
            print(1)
        elif(d > rb+rj):
            print(0)