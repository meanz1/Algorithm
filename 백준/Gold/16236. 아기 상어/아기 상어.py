from collections import deque
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
shark_x, shark_y = 0, 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0
shark_size = 2
ate = 0
for i in range(n):
    for j in range(n):
        if map[i][j] == 9:
            shark_x, shark_y = i, j
            break
def shark_search(shark_x, shark_y):
    global time
    global shark_size
    global ate
    while True:
        cand = BFS(shark_x, shark_y)
        if not cand:
            break
        time += cand[0]
        map[cand[1]][cand[2]] = 0 
        shark_x, shark_y = cand[1], cand[2]
        ate+=1        
        if shark_size == ate:
            shark_size+=1
            ate = 0    
    return time
def BFS(sx, sy):
    global shark_size
    q = deque()
    q.append((0, sx, sy)) #거리 행 열 순으로 정렬할거니까. 
    map[sx][sy] = 0
    food=[]
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    while q:    
        cur_d, cur_x, cur_y = q.popleft()       
        for x, y in dir:
            nx = cur_x + x
            ny = cur_y + y            
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if 0<=map[nx][ny]<=shark_size:
                    visited[nx][ny] = True
                    n_d =cur_d+1
                    q.append((n_d, nx, ny))
                if map[nx][ny] !=0 and map[nx][ny] < shark_size:
                    food.append((n_d, nx, ny))                    
    if food:
        food.sort()
        return food[0] 
    else:
        return  
print(shark_search(shark_x, shark_y))