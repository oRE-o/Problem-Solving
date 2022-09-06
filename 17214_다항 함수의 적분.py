f = input()
a = 0
b = 0

if (f.find('x') == -1): # b 
    b = int(f)

elif (f[-1] == 'x'): # ax 
    f = f.replace('x', '')
    a = int(f)
    b = 0

else: #ax+b 
    f = f.replace('x', ' ')
    a, b = map(int, f.split())

# b
if (a == 0):
    if (b == 0): # b == 0
        print('', end='')
    elif (b == 1): # b == 1
        print('x+', end='')
    elif (b == -1): # b == -1
        print('-x+', end='')     
    else: # else
        print(str(b) + 'x+', end='')
    print('W')

# ax
elif (a != 0 and b == 0):
    if (a // 2 == 1): # a == 1
        print('xx+', end='')
    elif (a // 2 == -1): # a == -1
        print('-xx+', end='')
    else: # else
        print(str(a//2)+'xx+', end='')
    print('W')

# ax+b
elif (a != 0 and b != 0):
    # xx 항 처리
    if (a // 2 == 1): # a == 1
        print('xx', end='')
    elif (a // 2 == -1): # a == -1
        print('-xx', end='')
    else: # else
        print(str(a//2)+'xx', end='')

    # 연산자 출력 
    if (b > 0):
        print('+', end='')

    # x항 처리
    if (b == 1): # b == 1
        print('x+', end='')
    elif (b == -1): # b == -1
        print('-x+', end='')     
    else: # else
        print(str(b) + 'x+', end='')
    
    print('W')
