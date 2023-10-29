import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
cand = []
for i in range(n):
  cand.append(i)

result = list(combinations(cand, k))

print(len(result))