import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

d = [0]*n
d[0] = nums[0]
ans = d[k-1]
for i in range(1, n):
    d[i] = d[i-1] + nums[i]
ans = d[k-1]
j = 0
for i in range(k, n):
    ans = max(ans, d[i]-d[j])
    j += 1

print(ans)