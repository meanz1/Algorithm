import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict_id = {}
dict_name = {}

for i in range(1, n+1):
  temp = input().rstrip()
  dict_name[temp] = i
  dict_id[i] = temp

for _ in range(m):
  temp = input().rstrip()
  if temp.isdigit():
    print(dict_id[int(temp)])
  else:
    print(dict_name[temp])

