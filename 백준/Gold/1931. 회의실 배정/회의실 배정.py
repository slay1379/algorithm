import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq

N = int(input())
meetings = []
for _ in range(N):
    start,end = map(int,input().split())
    meetings.append((start,end))

meetings = sorted(meetings,key=lambda x:(x[1],x[0]))
answer = 0
now_end = 0

for start,end in meetings:
    if start >= now_end:
        now_end = end
        answer += 1

print(answer)