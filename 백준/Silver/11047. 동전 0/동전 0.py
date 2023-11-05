import sys

input = sys.stdin.readline
n, k = map(int, input().split())

result = 0

coins = [
  int(input()) for _ in range(n)
]

new_coins = sorted(coins, reverse = True)
for elem in new_coins:
  if k // elem == 0:
    continue
  result += k//elem
  k %= elem

print(result)
