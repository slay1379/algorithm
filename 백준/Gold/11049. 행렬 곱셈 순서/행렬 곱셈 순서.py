import sys
input = sys.stdin.readline
from collections import deque
import heapq


def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1  # 행렬의 개수

    # dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱하는데 필요한 최소 연산 횟수
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 연쇄 길이 l을 2부터 n까지 증가시키며 계산
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = float('inf')  # 초기값을 무한대로 설정

            # i부터 j까지의 행렬을 곱할 때, 어느 지점에서 나눌지 결정
            for k in range(i, j):
                # A_i × ... × A_k와 A_(k+1) × ... × A_j로 나누어 계산
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


def main():
    n = int(input())  # 행렬의 개수

    # 각 행렬의 크기를 저장
    matrices = []
    for _ in range(n):
        r, c = map(int, input().split())
        matrices.append((r, c))

    # dimensions 배열 생성
    dimensions = [matrices[0][0]]
    for matrix in matrices:
        dimensions.append(matrix[1])

    # 최소 연산 횟수 계산
    min_operations = matrix_chain_multiplication(dimensions)
    print(min_operations)


if __name__ == "__main__":
    main()