x = int(input())
f = [0] * 46
f[1] = 2
f[2] = 3
f[3] = 5

for i in range(4, 46):
    f[i] = f[i-1] + f[i-2]

for i in range(x):
    n = int(input())
    print("Scenario #"+str((i+1))+": "+str(f[n])+"\n")