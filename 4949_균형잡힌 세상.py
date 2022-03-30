while(1):
    a = input()
    if a == '.':
        break
    
    sm = 0
    bi = 0

    for i in a:
        if i == '(':
            sm += 1
        if i == ')':
            sm -= 1
        if i == '[':
            bi += 1
        if i == ']':
            bi -= 1
    
    if sm == bi == 0:
        print('yes')
    else:
        print('no')