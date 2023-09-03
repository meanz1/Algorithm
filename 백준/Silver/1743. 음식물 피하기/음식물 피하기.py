from sys import setrecursionlimit
setrecursionlimit(10**5)
n, m, k = map(int, input().split())
#n = row, m = col
grid = [[0 for _ in range(m)] for _ in range(n)]

result = []
for _ in range(k):
    r_, c_ = map(int, input().split())
    grid[r_-1][c_-1] = 1

visited = [[False for _ in range(m)] for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(cur_x, cur_y):
    size = 1
    visited[cur_x][cur_y] = 1
    for dx, dy in direction:
        nx = cur_x + dx
        ny = cur_y + dy
        if 0<=nx<n and 0<=ny<m:
            if grid[nx][ny]==1 and not visited[nx][ny]:
                size += DFS(nx, ny)
    return size

for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == 1:
            result.append(DFS(i, j))
print(max(result))