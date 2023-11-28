import sys
from collections import deque

input = sys.stdin.readline
INT_MAX = sys.maxsize

m, n, h = map(int, input().split())
grid = []

q = deque()
for i in range(h):
  temp = []
  for j in range(n):
    temp.append(list(map(int, input().split())))
    for k in range(m):
      if temp[j][k] == 1:
        q.append((i, j, k))
  grid.append(temp)

dxs, dys, dzs = [-1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

while q:
  x, y, z = q.popleft();
  for dx, dy, dz in zip(dxs, dys, dzs):
    nx, ny, nz = x+dx, y+dy, z+dz
    if 0<=nx<h and 0<=ny<n and 0<=nz<m and grid[nx][ny][nz] == 0:
      q.append((nx, ny, nz))
      grid[nx][ny][nz] = grid[x][y][z]+1

day = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if grid[i][j][k] == 0:
        print(-1)
        exit(0)
    day = max(day, max(grid[i][j]))
print(day-1)