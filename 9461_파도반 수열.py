x = int(input())

tri = [0] * 101
tri[1] = 1
tri[2] = 1
tri[3] = 1

for i in range(4, 101):
    tri[i] = tri[i-2] + tri[i-3]

for i in range(x):
    n = int(input())
    print(tri[n])
