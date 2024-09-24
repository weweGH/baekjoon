def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    A.sort()
    B.sort(reverse=True)
    answer_pre = []
    for i in range(len(A)):
        ans = A[i]*B[i]
        answer_pre.append(ans)
    #
    answer = sum(answer_pre)
        
    return answer