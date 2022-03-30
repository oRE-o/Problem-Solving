x = int(input())
sc = [0] * (x+1)
for i in range(1, x+1):
    sc[i] = int(input())

f = [0] * (x+1)
if x == 1:
    print(sc[1])
    exit()
if x == 2:
    print(sc[1] + sc[2])
    exit()
if x == 3 :     
    print(max(sc[1], sc[2]) + sc[3])
    exit()

f[1] = sc[1] # 10
f[2] = sc[1] + sc[2] # 30
f[3] = max(sc[1], sc[2]) + sc[3] #35
#55, 65
for i in range(4, x+1):
    f[i] = max(f[i-2], f[i-3]+sc[i-1]) + sc[i]
print(f[x])