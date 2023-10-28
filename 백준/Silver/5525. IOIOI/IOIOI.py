import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

comparison = 'I' + 'OI'*n

cursor, cnt, result = 0, 0, 0
while cursor < (m-1):
  if s[cursor:cursor+3] == 'IOI':
    cnt += 1
    cursor+=2
    if cnt == n:
      result+=1
      cnt -=1
  else:
    cursor +=1
    cnt = 0

print(result)