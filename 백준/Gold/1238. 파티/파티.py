import sys
import heapq

input = sys.stdin.readline
INT_MAX = sys.maxsize
n, m, x = map(int, input().split())

pq = []
go_graph = [
  [] for _ in range(n+1)
]
back_graph = [
  [] for _ in range(n+1)
]

go_dist = [INT_MAX]*(n+1)
back_dist = [INT_MAX]*(n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  go_graph[a].append((b, c))
  back_graph[b].append((a, c))

go_dist[x] = 0
heapq.heappush(pq, (0, x))

while pq:
  min_dist, min_idx = heapq.heappop(pq)
  if go_dist[min_idx] != min_dist:
    continue
  for target_idx, target_dist in go_graph[min_idx]:
    new_dist = go_dist[min_idx] + target_dist
    if go_dist[target_idx] > new_dist:
      go_dist[target_idx] = new_dist
      heapq.heappush(pq, (new_dist, target_idx))

back_dist[x] = 0
heapq.heappush(pq, (0, x))

while pq:
  min_dist, min_idx = heapq.heappop(pq)
  if back_dist[min_idx] != min_dist:
    continue
  for target_idx, target_dist in back_graph[min_idx]:
    new_dist = back_dist[min_idx] + target_dist
    if back_dist[target_idx] > new_dist:
      back_dist[target_idx] = new_dist
      heapq.heappush(pq, (new_dist, target_idx))
    
result = []
for i in range(1, n+1):
  result.append(go_dist[i]+back_dist[i])
print(max(result))