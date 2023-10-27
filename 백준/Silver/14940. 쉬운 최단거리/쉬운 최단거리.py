import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

grid = [
  list(map(int, sys.stdin.readline().split())) for _ in range(n)
]
result = [
  [-1]*m for _ in range(n)
]
visited = [
  [False]*m for _ in range(n)
]
dq = deque()

for i in range(n):
  for j in range(m):
    if grid[i][j] == 1:
      continue
    elif grid[i][j] == 2:
      start_x, start_y = i, j
      result[i][j] = 0
    elif grid[i][j] == 0:
      result[i][j] = 0

def bfs():
  dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
  while dq:
    x, y, z = dq.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = x+dx, y+dy
      if 0<=nx<n and 0<=ny<m:
        if grid[nx][ny] != 0 and not visited[nx][ny]:
          result[nx][ny] = z+1
          visited[nx][ny] = True
          dq.append((nx, ny, z+1))
  return

visited[start_x][start_y] = True
dq.append((start_x, start_y, 0))
bfs()

for elem in result:
  print(*elem)

