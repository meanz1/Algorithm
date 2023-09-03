a, b = map(int, input().split())

value = [0]
for i in range(46):
    for j in range(i):
        value.append(i)
        

print(sum(value[a:b+1]))