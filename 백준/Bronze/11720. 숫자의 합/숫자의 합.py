import sys
input = sys.stdin.readline

n = int(input())
nums = input()

result = 0
for i in range(n):
    result += int(nums[i])
print(result)