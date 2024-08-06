def solution(x, n):
    
    answer = []
    x1 = x
    for number in range(0, n):

        if number == 0:
            answer.append(x)
        else:
            x1 = x1 + x
            answer.append(x1)
    return answer