def solution(num1, num2):
    if (0 < num1 <= 100) & (0 < num2 <= 100):
        answer = int(num1/num2*1000)
    
    return answer

solution(3,2)