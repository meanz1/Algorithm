n = int(input())
a = list(map(int, input().split())) #len(a) == n
b, c = map(int, input().split())

answer = n
for v in a:
    if v-b <= 0:
        continue
    else:
        if v-b <= c:
            answer+=1
            
        elif (v-b) % c == 0:
            answer += (v-b)//c
        elif (v-b)%c != 0:
            answer+= (v-b)//c +1
    

print(answer)