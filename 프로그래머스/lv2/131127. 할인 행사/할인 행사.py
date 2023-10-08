from collections import Counter
def solution(want, number, discount):
    order = {}
    answer = 0
    
    for i in range(len(want)):
        order[want[i]] = number[i]
        
    for i in range(len(discount)-9):
        temp_dic = dict(Counter(discount[i:i+10]))
        temp = 0
        for key in order:
            if key in temp_dic:
                if temp_dic[key] >= order[key]:
                    temp += 1
            
        if temp == len(want):
            answer += 1
                
    return answer