isNotSelfnum = [0] * 10001

for i in range(1, 10001):
    if i+eval('+'.join(str(i))) <= 10000:
        isNotSelfnum[i+eval('+'.join(str(i)))] = 1    

for i in range(1, 10001):
    if isNotSelfnum[i] != 1:
        print(i)