def solution(n):
    if 0 < n <= 1000:
        num_list = range(0,n+1)
        num_list = [x for x in num_list if x%2==0]
        answer = sum(num_list)
    return answer

solution(10)