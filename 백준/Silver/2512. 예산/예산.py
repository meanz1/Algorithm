import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())

start, end = 0, max(req)
total = 0

if sum(req) < m:
    print(max(req))
else:
    while start <= end:
        mid = (start+end)//2
        total = 0
        for elem in req:
            if elem > mid:
                total += mid
            else:
                total += elem
        
        if total <= m:
            start = mid +1
        else:
            end = mid - 1
    print(end)
