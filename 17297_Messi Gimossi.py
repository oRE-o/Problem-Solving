m = int(input())
messi = [''] * 3

messi[1] = "Messi"
messi[2] = "Messi Gimossi"

# 공백 수        0 > 1 > 2 > 4 > 7 > 12
# 순수 문자열     5 > 12 > 17 > 29 > 

while(len(messi[1]) < m or len(messi[2]) < m):
    messi[1] = messi[2] + ' ' + messi[1]
    messi[2] = messi[1] + ' ' + messi[2]

print(messi[2][m-1])