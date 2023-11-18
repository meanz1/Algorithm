import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

d = nums[:]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            d[i] = max(d[i], d[j]+nums[i])

print(max(d))