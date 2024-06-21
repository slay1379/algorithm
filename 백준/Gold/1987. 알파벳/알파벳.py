import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq


def dfs(x, y, visited, count):
    global answer
    answer = max(answer, count)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < R and 0 <= ny < C:
            char_bit = 1 << (ord(board[nx][ny]) - ord('A'))
            if not (visited & char_bit):
                new_visited = visited | char_bit
                if (nx, ny, new_visited) not in memo:
                    memo.add((nx, ny, new_visited))
                    dfs(nx, ny, new_visited, count + 1)


R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]
visited = 1 << (ord(board[0][0]) - ord('A'))
answer = 1
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
memo = set()

dfs(0, 0, visited, 1)
print(answer)
