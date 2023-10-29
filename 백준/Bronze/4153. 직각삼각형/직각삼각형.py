import sys
from itertools import permutations
input = sys.stdin.readline

while True:
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0:
    break
  cand = []
  cand.append(a)
  cand.append(b)
  cand.append(c)
  cand.sort()

  if cand[2]**2 == cand[0]**2 + cand[1]**2:
    print("right")
  else:
    print("wrong")
