import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
grid = [
    list(input()) for _ in range(n)
]
visited = [
    [False]*n for _ in range(n)
]

q = deque()
result = []
def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+ dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if grid[nx][ny]=='1' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    result.append(cnt)

    return

for i in range(n):
    for j in range(n):
        if grid[i][j] == '1' and not visited[i][j]:
            q.append((i, j))
            visited[i][j] = True
            bfs()

print(len(result))
result.sort()
for elem in result:
    print(elem)

