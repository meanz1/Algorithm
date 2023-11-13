import sys

input = sys.stdin.readline
n, m = map(int, input().split())

trees = list(map(int, input().split()))

top = max(trees)
bottom = 1

while bottom <= top:
    cnt = 0
    half = (bottom+top)//2
    for elem in trees:
        if elem > half:
            cnt += elem-half
    
    if cnt >= m:
        bottom = half+1
    elif cnt < m:
        top = half-1

print(top)