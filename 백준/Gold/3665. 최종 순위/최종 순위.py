import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


def find_rank():
    q = deque()
    answer = []

    for i in range(1, len(degree)):
        if degree[i] == 0:
            q.append(i)

    multiple_candidates = False

    while q:
        if len(q) > 1:
            multiple_candidates = True

        now = q.popleft()
        answer.append(now)

        for next in graph[now]:
            degree[next] -= 1
            if degree[next] == 0:
                q.append(next)

    if len(answer) != len(degree) - 1:
        return None
    if multiple_candidates:
        return -1

    return answer


t = int(input())
for _ in range(t):
    n = int(input())
    last_rank = list(map(int,input().split()))

    degree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1,n):
            graph[last_rank[i]].append(last_rank[j])
            degree[last_rank[j]] += 1

    m = int(input())
    if m == 0:
        print(' '.join(map(str,last_rank)))
        continue
    for _ in range(m):
        a,b = map(int,input().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            degree[b] += 1
            degree[a] -= 1


    answer = find_rank()
    if answer == None:
        print("IMPOSSIBLE")
    elif answer == -1:
        print("?")
    else:
        print(' '.join(map(str, answer)))
