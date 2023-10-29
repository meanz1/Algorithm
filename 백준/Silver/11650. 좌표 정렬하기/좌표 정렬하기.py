import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
  a, b = map(int, input().split())
  result.append((a, b))

result.sort()
for elem in result:
  print(elem[0], elem[1])