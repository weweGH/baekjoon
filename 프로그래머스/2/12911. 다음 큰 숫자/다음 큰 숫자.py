def solution(n):
    # n의 이진수에서 1의 개수를 센다.
    count_ones = bin(n).count('1')
    
    # n보다 큰 수 중에서 1의 개수가 같은 가장 작은 수를 찾는다.
    next_number = n + 1
    while True:
        if bin(next_number).count('1') == count_ones:
            return next_number
        next_number += 1
