import sys

input = sys.stdin.readline
n, c = map(int, input().split())
things = [
    int(input()) for _ in range(n)
]

things.sort()

start, end = 1, things[-1]-things[0]

if c == 2:
    print(things[-1]-things[0])
else:
    while (start < end):
        cnt = 1
        mid = (start+end)//2

        recent = things[0]
        for i in range(n):
            if things[i]-recent >= mid:
                cnt += 1
                recent = things[i]
        if cnt >= c:
            result = mid
            start = mid + 1
        else:
            end = mid
    print(result)
