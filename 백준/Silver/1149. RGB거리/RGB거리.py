import sys
input = sys.stdin.readline
n = int(input())

grid = [
    list(map(int, input().split())) for _ in range(n)
]

for i in range(1, n):
    grid[i][0] = min(grid[i-1][1], grid[i-1][2]) + grid[i][0]
    grid[i][1] = min(grid[i-1][0], grid[i-1][2]) + grid[i][1]
    grid[i][2] = min(grid[i-1][0], grid[i-1][1]) + grid[i][2]

print(min(grid[n-1][0], grid[n-1][1], grid[n-1][2]))