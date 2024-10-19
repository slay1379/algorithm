import sys
import re

input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq


def solution(board):
    N = len(board)
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌

    # (x, y, 비용, 방향)
    queue = deque([(0, 0, 0, -1)])  # 초기 방향은 -1로 설정
    for i in range(4):
        cost[0][0][i] = 0

    while queue:
        x, y, current_cost, prev_direction = queue.popleft()

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = current_cost + 100
                if prev_direction != -1 and prev_direction != i:
                    new_cost += 500  # 코너 비용 추가

                if new_cost < cost[nx][ny][i]:
                    cost[nx][ny][i] = new_cost
                    queue.append((nx, ny, new_cost, i))

    # 도착점의 최소 비용 구하기
    return min(cost[N-1][N-1])

