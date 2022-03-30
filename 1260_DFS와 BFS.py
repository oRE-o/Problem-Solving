from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  q = deque() # 너비 우선 탐색은 Queue 로 이루어진다
  q.append(v) # 우선 탐색열에 v 추가
  visit_list[v] = 1 # visit으로 표시함
  while q: # 빌때까지 계속
    v = q.popleft() # 탐색열에서 pop 시킨걸 새로운 V로 지정
    print(v, end = " ") # 그걸 탐색한거니까 출력
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1: # 그 점과 이어진 인접 정점들을 싹 다 돌면서 있는대로 
        q.append(i) # 탐색리스트에 추가
        visit_list[i] = 1 # 방문되었다는 걸 표시
        # 위에서 다시 새로운 v에 대해 시작할거고, queue이므로 1단계 탐색에 대해 먼저 다 뽑고 나서 그다음 탐색이 차례대로 됨
        # 한번 훑은 곳은 다시 기준으로 잡진 않는다.

def dfs(v):
  visit_list2[v] = 1 # v에 대해 방문,
  print(v, end = " ") # 방문한거 확인하고 프린트.
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i) # 일부가 전체와 같은 탐색의 구조를 띄므로 재귀.
      # 이어진 정점에서 재귀적으로 탐색을 진행한다.

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1 # 이어져 있는 걸 표시하는 것

dfs(v) # v는 탐색을 시작하는 정점
print()
bfs(v)