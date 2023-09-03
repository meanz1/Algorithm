n = int(input())
value = list(map(int, input().split()))
oper = list(map(int, input().split())) # +-x%
maximum = -1e9
minimum = 1e9

def DFS(depth, total, plus, minus, mul, div):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
    if plus:
        DFS(depth+1, total+value[depth], plus-1, minus, mul, div)
    if minus:
        DFS(depth+1, total-value[depth], plus, minus-1, mul, div)
    if mul:
        DFS(depth+1, total*value[depth], plus, minus, mul-1, div)
    if div:
        DFS(depth+1, int(total/value[depth]), plus, minus, mul, div-1)

DFS(1, value[0], oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)

    