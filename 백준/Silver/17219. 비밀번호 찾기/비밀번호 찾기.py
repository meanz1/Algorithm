import sys
n, m = map(int, sys.stdin.readline().split())

keyValue = {}
for _ in range(n):
  a, b = input().split()
  keyValue[a] = b

for _ in range(m):
  findKey = sys.stdin.readline().rstrip()
  print(keyValue[findKey])