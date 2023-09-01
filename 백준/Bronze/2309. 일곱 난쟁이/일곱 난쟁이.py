value = [int(input()) for _ in range(9)]
all_v = sum(value)
result = False

for i in range(8):
    for j in range(i+1, 9):
        if (all_v - (value[i] + value[j]) == 100):
            save = [i, j]
            
            result = False
            break
    if result:
        break
del value[save[0]]
del value[save[1]-1]

value.sort()

for i in value:
    print(i)

