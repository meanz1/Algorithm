import heapq
import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize
v, e = map(int, input().split())
s = int(input())
grid = [
  [] for _ in range(v+1)
]

dist = [INT_MAX]*(v+1)
pq = []
for i in range(e):
  a, b, c = map(int, input().split())
  grid[a].append((b, c))

heapq.heappush(pq, (0, s))
dist[s] = 0
while pq:
  min_dist, min_idx = heapq.heappop(pq)

  if min_dist != dist[min_idx]:
    continue
  for target_idx, target_dist in grid[min_idx]:
    new_dist = dist[min_idx] + target_dist
    if dist[target_idx] > new_dist:
      dist[target_idx] = new_dist
      heapq.heappush(pq, (new_dist, target_idx))

for i in range(1, v+1):
  if dist[i] == INT_MAX:
    print("INF")
  else:
    print(dist[i])