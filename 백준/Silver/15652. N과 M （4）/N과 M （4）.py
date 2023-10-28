import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

cand = []
for i in range(1, n+1):
  cand.append(i)

result = list(combinations_with_replacement(cand, m))
result.sort()

for elem in result:
  print(*elem)
