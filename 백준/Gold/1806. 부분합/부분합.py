import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = [0]+list(map(int, input().split()))

j = 0
sum_v = 0
ans = sys.maxsize
for i in range(1, n+1):
    while j+1<=n and sum_v < s:
        j +=1
        sum_v+= nums[j]
  
    if sum_v < s:
        break
    ans = min(ans, j-i+1)

    sum_v -= nums[i]
        
if ans == sys.maxsize:
    ans = 0
print(ans)