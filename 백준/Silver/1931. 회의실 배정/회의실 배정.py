import sys

input = sys.stdin.readline
n = int(input())

con = []
for _ in range(n):
  a, b = map(int, input().split())
  con.append((a, b))

new_con = sorted(con, key=lambda x: (x[1], x[0]))
cnt = 1

start = new_con[0][1]

for i in range(1, len(new_con)):
  a, b = new_con[i]

  if a >= start:
    start = b
    cnt += 1

print(cnt)