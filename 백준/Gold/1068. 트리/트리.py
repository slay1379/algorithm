import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N = int(input())
line = list(map(int,input().split()))
d = int(input())

graph = [[] for _ in range(len(line))]

for i,node in enumerate(line):
    if node == -1:
        continue
    graph[node].append(i)

q = deque()
q.append(d)

if line[d] != -1:
    graph[line[d]].remove(d)

while q:
    now = q.popleft()
    for next in graph[now]:
        q.append(next)
    graph[now] = [-1]

answer = 0
for nodes in graph:
    if len(nodes) == 0:
        answer += 1

print(answer)