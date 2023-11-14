import sys

input = sys.stdin.readline
n = int(input())

card = dict()

mine = list(map(int, input().split()))
m = int(input())
comp = list(map(int, input().split()))
for elem in mine:
    card[elem] = 1
result = []
for elem in comp:
    if elem in card:
        result.append(1)
    else:
        result.append(0)

print(*result)