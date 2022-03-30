a= int(input())
b = a
c = 1
while(1):
    b = (b%10)*10 + (b//10 + b%10)%10
    if (b==a):
        break
    else:
        c= c+1
print(c)