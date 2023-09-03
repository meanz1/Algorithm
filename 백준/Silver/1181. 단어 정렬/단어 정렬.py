import sys
n = int(sys.stdin.readline())

words = []

for _ in range(n):
  words.append(sys.stdin.readline().strip())

word_set = set(words)
word_list = list(word_set)

word_list.sort()
word_list.sort(key=len)

for elem in word_list:
  print(elem)