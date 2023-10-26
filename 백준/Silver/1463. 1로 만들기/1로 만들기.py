import sys
n = int(input())

cnt = 0
dp = [sys.maxsize]*(n+1)
dp[1] = 0

for i in range(2, n+1):
  dp[i] = dp[i-1] + 1
  if i%2 == 0:
    dp[i] = min(dp[i//2]+1, dp[i])
  if i%3 ==0:
    dp[i] = min(dp[i//3]+1, dp[i])


print(dp[n])
