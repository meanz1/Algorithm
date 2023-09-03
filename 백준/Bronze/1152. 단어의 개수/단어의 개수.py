line = input()
line_split = line.split(' ')

result = 0
for elem in line_split:
  if elem != '':
    result += 1

print(result)