import sys
from collections import deque

input = sys.stdin.readline
INT_MAX = sys.maxsize

n = int(input())
grid = []
for i in range(n):
  grid.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(len(grid[i])):
    if j == 0:
      grid[i][j]= grid[i][j]+ grid[i-1][j]
    elif j== len(grid[i])-1:
      grid[i][j] = grid[i][j] + grid[i-1][j-1]
    else:
      grid[i][j] = max(grid[i-1][j-1], grid[i-1][j])+grid[i][j]

print(max(grid[n-1]))