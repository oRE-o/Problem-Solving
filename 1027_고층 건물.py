import sys

def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

N = int(sys.stdin.readline())
building = list(map(int,sys.stdin.readline().split()))
answer = 0
for index, b in enumerate(building):
    view_max = 0
    left_max = float('inf') # 왼쪽의 기울기 최솟값
    right_max = -float('inf') # 오른쪽 기울기 최댓값

    for i in range(index-1, -1, -1):  # 왼쪽
        c = slope(index+1, b, i+1, building[i]) 
        if c < left_max: # 기울기가 더 작다면
            left_max = c 
            view_max += 1

    for i in range(index+1,N):  # 오른쪽
        c = slope(index+1, b, i+1, building[i])
        if c > right_max: # 기울기가 더 크다면
            right_max = c
            view_max += 1

    answer = max(answer, view_max)
print(answer)