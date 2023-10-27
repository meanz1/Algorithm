n = int(input())
times = list(map(int, input().split()))

times.sort()
result = 0
for i in range(1, n+1):
  result += sum(times[:i])

print(result)