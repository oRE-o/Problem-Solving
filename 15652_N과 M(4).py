n, m = map(int, input().split())
s = []

def dfs(j): 
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(j, n + 1): # 어떤 숫자보다 크거나 같은 숫자부터 진행
    s.append(i)
    dfs(i)
    s.pop()

dfs(1)