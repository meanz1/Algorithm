import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

visited = [False]*100001
q = deque()
q.append((n, 0))
visited[n] = True

while q:
  x, z = q.popleft()

  if x == k:
    print(z)
    break
  arr = [x-1, x+1, x*2]
  for elem in arr:
    if 0<=elem<=100000 and not visited[elem]:
        visited[elem] = True
        q.append((elem, z+1))
