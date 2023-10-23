import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
new_scores = []
m = max(scores)
for elem in scores:
  new_scores.append(elem/m*100)
print(sum(new_scores)/len(new_scores))
