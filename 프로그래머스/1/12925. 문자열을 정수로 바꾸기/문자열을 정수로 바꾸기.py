def solution(s):
    
    answer_pre = list(map(str, s))
    answer = answer_pre[0]
    for aa in answer_pre[1:]:
        answer = answer + aa
    return int(answer)