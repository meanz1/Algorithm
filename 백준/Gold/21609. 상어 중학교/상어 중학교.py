from collections import deque
n, m = map(int, input().split())
# n, m = 5, 3
# block = [[2, 2, -1, 3, 1], [3, 3, 2, 0, -1], [0, 0, 0, 1, 2], [-1, 3, 1, 3, 2], [0, 3, 2, 2, 1]]
block = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
score = 0

def find_block(i, j, block_num):
    q = deque()
    q.append((i, j))
    
    rainbows= []
    normals = [[i, j]]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and block[nx][ny] == 0:
                    q.append((nx, ny))
                    rainbows.append([nx, ny])
                    visited[nx][ny] = 1

                elif not visited[nx][ny] and block[nx][ny] == block_num:
                    q.append((nx, ny))
                    normals.append([nx, ny])
                    visited[nx][ny] = 1
        
    for x, y in rainbows:
        visited[x][y] = 0
            
    
    return [len(normals+rainbows), len(rainbows), normals+rainbows]

def remove_block(group):
    global score
    score += group[0]**2
    for x, y in group[2]:
        block[x][y] = -2
    return
        

    
def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if block[i][j] != -1:
                pointer = i
                
                while pointer+1 < n and block[pointer+1][j] == -2:
                    block [pointer+1][j] = block[pointer][j]
                    block[pointer][j] = -2
                    pointer+=1
    return
    
def rotate_block():
    global block
    temp = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-1-j][i] = block[i][j]
        
    block = temp
    return 
    
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    groups = [] #블록 그룹 저장
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and block[i][j] >= 1:
                visited[i][j] = 1
                group = find_block(i, j, block[i][j])
                
                if group[0] >=2 :
                    groups.append(group)
    
    groups.sort(reverse=True)
    
    if not groups:
        break

    remove_block(groups[0])
    gravity()
    rotate_block()
    gravity()
    
    
print(score)
    
    