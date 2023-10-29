import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
cand = list(map(int, input().split()))
dist = m
result = 0
result = list(permutations(cand, 3))
for elem in result:
  val = sum(elem)
  if val > m:
    continue
  if abs(val-m) < dist:
    result = val
    dist = abs(val-m)
  
print(result)