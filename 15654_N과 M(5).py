n, m = map(int, input().split())
li = list(map(int, input().split()))

li.sort()

s = []

def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(0, n):
    if li[i] in s:
      continue

    s.append(li[i])
    dfs()
    s.pop()

dfs()