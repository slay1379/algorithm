import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
times = []
answer = 0
for _ in range(N):
    start, end = map(int,input().split())
    times.append((start,end))

times.sort(key=lambda x : (x[1], x[0]))

now = 0
for start, end in times:
    if start >= now:
        now = end
        answer += 1

print(answer)