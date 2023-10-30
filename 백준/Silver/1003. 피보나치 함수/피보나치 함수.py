import sys

input = sys.stdin.readline

t = int(input())

dp1 = [0]*42
dp0 = [0]*42
dp0[0] = 1
dp1[0] = 0
dp0[1] = 0
dp1[1] = 1

for i in range(2, 42):
  dp0[i] = dp0[i-1] + dp0[i-2] 
  dp1[i] = dp1[i-1] + dp1[i-2] 

for _ in range(t):
  t = int(input())
  print(dp0[t], dp1[t])

