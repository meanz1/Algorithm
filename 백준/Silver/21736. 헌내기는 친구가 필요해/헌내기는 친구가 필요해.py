import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

q = deque()
grid = [
  list(sys.stdin.readline().rstrip()) for _ in range(n)
]

visited = [
  [False] * m for _ in range(n)
]

cnt = 0

for i in range(n):
  for j in range(m):
    if grid[i][j] == 'I':
      q.append((i, j))
      visited[i][j] = True

def can_go(x, y):
  return 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] != 'X'

def bfs():
  global cnt
  dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
  while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
      nx, ny = dx + x, dy + y
      if (can_go(nx, ny)):
        if grid[nx][ny] == 'P':
          cnt += 1
        q.append((nx, ny))
        visited[nx][ny] = True

bfs()
if cnt == 0:
  print('TT')
else:
  print(cnt)
