n = int(input())

p = input().split()
nimsum = 0

for i in p:
    nimsum ^= int(i)

if nimsum == 0:
    print('cubelover')
else:
    print('koosaga')