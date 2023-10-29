import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(1, n+1):
  q.append(i)

while len(q) > 1:
  q.popleft()
  if len(q) == 1:
    break
  q.append(q.popleft())
print(q.popleft())