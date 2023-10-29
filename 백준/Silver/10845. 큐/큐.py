import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
  elem = list(input().split())
  if elem[0] == 'push':
    q.append(int(elem[1]))
  elif elem[0] == 'pop':
    if len(q) == 0:
      print(-1)
    else:
      print(q.popleft())
  elif elem[0] == 'size':
    print(len(q))
  elif elem[0] == 'empty':
    if len(q):
      print(0)
    else:
      print(1)
  elif elem[0] == 'front':
    if len(q):
      print(q[0])
    else:
      print(-1)
  elif elem[0] == 'back':
    if len(q):
      print(q[-1])
    else:
      print(-1)