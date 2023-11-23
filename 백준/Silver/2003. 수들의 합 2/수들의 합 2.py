import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]+list(map(int, input().split()))

j = 0
sum_v = 0
cnt = 0
for i in range(1, n+1):
    while j+1<=n and sum_v+nums[j+1] <= m:
        j +=1
        sum_v+= nums[j]
  
    if sum_v ==m:
        cnt+=1
       
    sum_v -= nums[i]
        

print(cnt)