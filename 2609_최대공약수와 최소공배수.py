a, b = map(int, input().split())

for i in range(max(a,b), 0, -1):
    if a%i == 0 and b%i == 0:
        gcd = i
        print(i)
        break

print((a*b)//i)