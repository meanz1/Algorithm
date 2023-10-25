import sys
n = int(input())
result = set()

for _ in range(n):
  elem = list(sys.stdin.readline().strip().split())
  if elem[0] == 'add':
    result.add(int(elem[1]))
  elif elem[0] == 'remove':
    result.discard(int(elem[1]))
  elif elem[0] == 'check':
    if int(elem[1]) in result :
      print(1)
    else:
      print(0)
  elif elem[0] == 'toggle':
    if int(elem[1]) in result:
      result.discard(int(elem[1]))
    else:
      result.add(int(elem[1]))
  elif elem[0] == 'all':
    result = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
  elif elem[0] == 'empty':
    result = set()