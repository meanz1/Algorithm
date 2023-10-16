n = int(input())
m = int(input())
grid = [
  [] for _ in range(n+1)
]
visited = [0]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  grid[a] += [b]
  grid[b] += [a]

def dfs(v):
  visited[v] = 1
  for nx in grid[v]:
    if visited[nx] == 0:
      dfs(nx)

dfs(1)
print(sum(visited)-1)