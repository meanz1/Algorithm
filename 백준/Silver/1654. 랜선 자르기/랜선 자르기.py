import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = []
for _ in range(k):
  lans.append(int(input()))

start, end = 1, max(lans)

while start <= end:
  cnt = 0
  mid = (start+end)//2
  
  for elem in lans:
    cnt += elem//mid
  
  if cnt < n:
    end = mid - 1

  if cnt >= n:
    start = mid +1

print(end)
  