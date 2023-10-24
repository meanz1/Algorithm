import sys
import math
input = sys.stdin.readline

n = int(input())
num = math.factorial(n)

num = str(num)[::-1]

cnt = 0
for i in num:
  if i == '0':
    cnt += 1
  else:
    break

print(cnt)
