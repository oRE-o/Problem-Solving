cache = [0 for _ in range(15)]
cnt = 0

# 필요한 탐색인지 분기
def isPromising(row, col):
    for i in range(row):
        if cache[i] == col:
            return False
        if (cache[i]-col) == (i-row):
            return False
        if (cache[i]-col) == (row-i):
            return False
    return True

n = int(input())

def bt(row):
    global cnt
    if row == n:
        cnt += 1
        return
    
    for i in range(n):
        if isPromising(row, i+1):
            cache[row] = i+1
            bt(row+1)
        else:
            continue

bt(0)
print(cnt)