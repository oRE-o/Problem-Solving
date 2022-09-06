n, m = map(int, input().split())
s = []
def dfs():
  if len(s) == m: 
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1): # 1부터 4까지 조짐
    if i in s: 
      continue # 같은 숫자가 있을 경우 스킵
    s.append(i) # s 리스트에 겹치지 않는 숫자를 추가
    dfs() # 그 다음 숫자 계산 위해 재실행
    s.pop()

dfs()