def solution(board, skill):
    n = len(board)
    m = len(board[0])
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    # 스킬 정보를 prefix 배열에 기록
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        prefix[r1][c1] += degree
        prefix[r1][c2 + 1] -= degree
        prefix[r2 + 1][c1] -= degree
        prefix[r2 + 1][c2 + 1] += degree

    # 행 기준 누적합 계산
    for i in range(n):
        for j in range(1, m):
            prefix[i][j] += prefix[i][j - 1]

    # 열 기준 누적합 계산
    for j in range(m):
        for i in range(1, n):
            prefix[i][j] += prefix[i - 1][j]

    # 최종적으로 board에 반영하여 파괴되지 않은 건물의 수 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer