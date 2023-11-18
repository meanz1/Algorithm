import sys

input = sys.stdin.readline

s1 = input()
s2 = input()

dp = [
    [0]*(len(s2)) for _ in range(len(s1))
]

for r in range(1, len(s1)):
    for c in range(1, len(s2)):
        if s1[r-1] == s2[c-1]:
            dp[r][c] = dp[r-1][c-1]+1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])
print(dp[-1][-1])