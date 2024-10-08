def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    now = 0
    for b in B:
        if b>A[now]:
            answer += 1
            now += 1
    return answer