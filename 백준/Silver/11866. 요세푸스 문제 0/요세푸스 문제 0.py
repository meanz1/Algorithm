import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
cand = deque()
for i in range(1, n+1):
  cand.append(i)
result = []
cnt = 0
while cand:
  for i in range(k-1):
    cand.append(cand.popleft())
  result.append(cand.popleft())

result = result+list(cand)
answer = '<'
for elem in result:
  answer += str(elem)
  answer += ', '
answer = answer[:-2] + '>'
print(answer)
