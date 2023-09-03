from collections import deque
# m = row = x, n = col = y

def Maze(grid):
    depth = 0
    row = len(grid)
    col = len(grid[0])
    direction = [(-1, 0),(1, 0), (0, -1), (0, 1)]

    if grid[0][0] != '1' or grid[row-1][col-1] !='1':return depth
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while queue:
        cur_x, cur_y, cur_d = queue.popleft()
        
        if cur_x == row-1 and cur_y == col-1:
            depth = cur_d
            break
        
        for dx, dy in direction:
            n_x = cur_x + dx
            n_y = cur_y + dy
            if 0<=n_x<row and 0<=n_y<col :
                if grid[n_x][n_y] == '1':
                    if visited[n_x][n_y]==False:
                        queue.append((n_x, n_y, cur_d+1))
                        visited[n_x][n_y] = True
                
    return depth



m, n = map(int, input().split())
grid = [list(input()) for _ in range(m)]

print(Maze(grid))