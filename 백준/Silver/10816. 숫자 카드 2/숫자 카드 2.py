import sys
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
has = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

new_check = dict(Counter(has))
for elem in check:
  if elem in new_check:
    print(new_check[elem], end=" ")
  else:
    print(0, end=" ")