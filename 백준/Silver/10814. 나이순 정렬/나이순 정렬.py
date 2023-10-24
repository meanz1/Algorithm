import sys
n = int(input())

info = []
for _ in range(n):
  a, b = sys.stdin.readline().split()
  info.append((a, b))
new_info = sorted(info, key=lambda x: int(x[0]))
for elem in new_info:
  a, b = elem
  print(a, b)