import sys
sys.setrecursionlimit(10000)
t = int(sys.stdin.readline())
result = []
def dfs(x, y):
  dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

  for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy
    if 0<=nx<m and 0<=ny<n:
      if grid[ny][nx] == 1:
        grid[ny][nx] = -1
        dfs(nx, ny)

for _ in range(t):
  cnt = 0
  m, n, k = map(int, sys.stdin.readline().split())

  grid = [
    [0]*m for _ in range(n)
  ]

  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    grid[y][x] = 1

  for i in range(m):
    for j in range(n):
      if grid[j][i] > 0:
        dfs(i, j)
        cnt += 1
  result.append(cnt)

for elem in result:
  print(elem)