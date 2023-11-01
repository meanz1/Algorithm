import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

nums = [
  list(map(int, input().split())) for _ in range(n)
]

nums.sort(key = lambda x: (x[1], x[0]))
for a,b in nums:
  print(a, b)