from collections import deque

m, n = map(int, input().split())
grid = [
  list(map(int, input().split())) for _ in range(n)
]


tomatos = []

def can_go(x, y):
  return 0<=x<n and 0<=y<m and grid[x][y] == 0 

result = 0
q = deque()


for i in range(n):
  for j in range(m):
    if grid[i][j]==1:
      q.append((i, j))


dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
while q:
  cx, cy = q.popleft()
  for x, y in zip(dxs, dys):
    nx, ny = cx + x, cy + y
    if can_go(nx, ny):
      q.append((nx, ny))
      grid[nx][ny] = grid[cx][cy] + 1


for line in grid:
  for tomato in line:
    if tomato == 0:
      print(-1)
      exit()
  result = max(result, max(line))

print(result-1)