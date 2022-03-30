a = int(input())
b = int(input())
c = int(input())

multi = str(a * b * c)

for i in range(10):
    print(multi.count(str(i)))
