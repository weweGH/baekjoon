from statistics import mean

def solution(numbers):
    if 1 <= len(numbers) <= 100:
        answer = mean(numbers)
    return answer

solution([1,2,3,4,5,6,7,8,9,10])