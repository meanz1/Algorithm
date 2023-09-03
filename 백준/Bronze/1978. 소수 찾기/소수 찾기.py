k = int(input())
value = list(map(int, input().split()))

result_n = 0
for i in value:
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 2:
        result_n +=1
            
print(result_n)