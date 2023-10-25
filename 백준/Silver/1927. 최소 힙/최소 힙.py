import heapq
import sys

hq = []
n = int(input())

for _ in range(n):
  temp = int(sys.stdin.readline())
  if temp == 0:
    if len(hq):
      print(heapq.heappop(hq))
    else:
      print(0)
  else:
    heapq.heappush(hq, temp)