import heapq
import sys

n = int(input())
m = int(input())
MAX_V = int(1e9)

pq = []
graph = [
    [] for _ in range(n+1)
]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    
depart, arrival = map(int, sys.stdin.readline().split())
dist = [MAX_V] * (n+1)
# idx랑 거리 순
dist[depart] = 0
heapq.heappush(pq, (depart, 0))

while pq:
    min_idx, min_dist = heapq.heappop(pq)
    if dist[min_idx] != min_dist:
        continue

    for target_idx, target_dist in graph[min_idx]:
        new_dist = dist[min_idx] + target_dist
        if dist[target_idx] > new_dist:
            dist[target_idx] = new_dist
            heapq.heappush(pq, (target_idx, new_dist))

print(dist[arrival])
