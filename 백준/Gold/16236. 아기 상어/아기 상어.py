from collections import deque

n = int(input())
grid = [
  list(map(int, input().split())) for _ in range(n)
]

q = deque() # 먹이 찾을 때 BFS할 큐 만듦

dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0] # 상 좌 우 하 순으로

cx, cy = 0, 0 # 상어의 현재 위치
time = 0 # 최종 반환할 시간탐색
size = 2 # 상어의 초기 크기
must_eat = 0 # 성장을 위해 꼭 먹어야하는 물고기 수

for i in range(n):
  for j in range(n):
    if grid[i][j] == 9:
      cx, cy = i, j # 상어의 현재 위치 설정
      break

def in_range(x, y):
  return 0<=x<n and 0<=y<n


def bfs(cz, cx, cy):
  visited = [
    [False]*n for _ in range(n)
  ]
  q.append((cz, cx, cy))
  visited[cx][cy] = True
  result = []
  while q:
    z, x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
      nx, ny = x+dx, y+dy
      if(in_range(nx, ny) and not visited[nx][ny]):
        if(0 == grid[nx][ny] or grid[nx][ny] == size): # 지나갈 수만 있음
          q.append((z+1, nx, ny))
          visited[nx][ny] = True
          
        elif ( 0 < grid[nx][ny] < size): # 실질적으로 먹을 수 있는 것
          result.append((z+1, nx, ny))
          
        
  result.sort()
  if(len(result) > 0):
    return result[0]
  return 0;


def find_fish():
  global time, must_eat, size, grid
  global cx, cy
  while True:
    cand = bfs(0, cx, cy)
    grid[cx][cy] = 0

    if not cand: break # 후보 없으면 break

    time += cand[0]
    cx = cand[1]
    cy = cand[2]

    must_eat +=1
    if (must_eat == size):
      size += 1
      must_eat = 0
  return time

print(find_fish())