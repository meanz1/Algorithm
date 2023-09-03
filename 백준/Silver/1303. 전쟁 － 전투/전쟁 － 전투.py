from collections import deque

n, m = map(int, input().split())
maze = [list(input()) for _ in range(m)] # m = 행의 갯수, 세로 길이
visited = [[False for _ in range(n)] for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque([])
B, W = 0, 0

def BFS(x, y):
    queue.append([x, y])
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maze[x][y] == maze[nx][ny] and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            ans = BFS(i, j)
            if maze[i][j] == 'W':
                W += ans ** 2
            else:
                B += ans ** 2

print(W, B)
