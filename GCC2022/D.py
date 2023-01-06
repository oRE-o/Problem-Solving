import sys

string = str(sys.stdin.readline().rstrip())

# for i in string:
#     string.append(ord(i))

check = []
ans = 0
cnt_a = 0

for i in range(len(string)):
    if string[i] == 'A':
        # print('A발견')
        cnt_a += 1


    if string[i] == string[i-1] or ord(string[i]) == ord(string[i-1]) + 1 or i == 0:
        if string[i] == 'Z':
            # print('z발견, +',cnt_a)
            ans += cnt_a

    else:
        # print('짤림 at',i)
        cnt_a = 0
        if string[i] == 'A':
            cnt_a = 1

print(ans)