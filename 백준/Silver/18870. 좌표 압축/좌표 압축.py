import sys

input = sys.stdin.readline
n = int(input())

nums = list(map(int, input().split()))
new_nums = sorted(set(nums))

nums_dict = {}
for i in range(len(new_nums)):
  if new_nums[i] in nums_dict:
    continue
  nums_dict[new_nums[i]] = i

result = []
for elem in nums:
  result.append(nums_dict[elem])
print(*result)