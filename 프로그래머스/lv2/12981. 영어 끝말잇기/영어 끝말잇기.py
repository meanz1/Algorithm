def solution(n, words):
    answer = []
    ref = {}
    ref[words[0]] = 1
    for i in range(1, len(words)):
        if words[i] in ref:
            answer.append(i%n +1) 
            answer.append(i//n+1)
            return answer
        ref[words[i]] = 1

        if words[i][0] != words[i-1][-1]:
            answer.append(i%n +1)
            answer.append(i//n+1)
            return answer
    answer = [0, 0]
    return answer