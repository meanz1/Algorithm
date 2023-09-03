n, m = map(int, input().split())
cnt = []
grid = []

for i in range(n):
  grid.append(input())

for a in range(n-7):
  for b in range(m-7):
    w_start = 0
    b_start = 0
    for i in range(a, a+8):
      for j in range(b, b+8):
        if (i+j)%2 == 0:
          if grid[i][j] != 'W':
            w_start += 1
          else:
            b_start += 1
        else:
          if grid[i][j] != 'W':
            b_start += 1
          else:
            w_start += 1
    cnt.append(w_start)
    cnt.append(b_start)

print(min(cnt))