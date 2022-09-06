n, m = map(int, input().split())
s = []
a = []

def dfs():
  if len(s) == m:
    if (set(s) not in a):
        print(' '.join(map(str, s)))
        a.append(set(s))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    dfs()
    s.pop()

dfs()