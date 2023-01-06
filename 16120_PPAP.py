li = input()

pcnt = 0
for i in range(len(li)):
    if li[i] == 'A':
        if i+1 == len(li) or (i+1 < len(li) and li[i+1] == 'A'):
            print('NP')
            exit()
        
        pcnt -= 2

        if pcnt < 0:
            print('NP')
            exit()

    elif li[i] == 'P':
        pcnt += 1

if pcnt == 1:
    print('PPAP')
else:
    print('NP')