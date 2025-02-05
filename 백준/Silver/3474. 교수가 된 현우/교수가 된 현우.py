import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    a = 0
    answer = 0
    N = int(input())
    now = 5
    while True:
        a += 1
        now = 5 ** a
        if now > N:
            break
        answer += (N//now)
    print(answer)