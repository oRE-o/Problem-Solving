s = input()
for i in range(len(s)):
    if s[i] == 'U':
        for j in range(i, len(s)):
            if s[j] == 'C':
                for k in range(j, len(s)):
                    if s[k] == 'P':
                        for l in range(k, len(s)):
                            if s[l] == 'C':
                                print('I love UCPC')
                                exit()
print('I hate UCPC')