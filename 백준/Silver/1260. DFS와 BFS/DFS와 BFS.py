from collections import deque

n, m, v = map(int, input().split())

grid = [
  [False]*(n+1) for _ in range(n+1)
]

for _ in range(m):
  a, b = map(int, input().split())
  grid[a][b] = True
  grid[b][a] = True

visitedB = [False] * (n+1)
visitedD = [False] * (n+1)

def bfs(v):
  q = deque([v])
  visitedB[v] = True

  while q:
    V = q.popleft()
    print(V, end=" ")
    for i in range(1, n+1):
      if not visitedB[i] and grid[V][i]:
        q.append(i)
        visitedB[i] = True
  
def dfs(v):
  visitedD[v] = True
  print(v, end=" ")

  for i in range(1, n+1):
    if not visitedD[i] and grid[v][i]:
      dfs(i)

dfs(v)
print()
bfs(v)