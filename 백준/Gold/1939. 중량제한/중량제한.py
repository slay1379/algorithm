import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def BFS(mid):
    q = deque([start])
    visit = [False]*(N+1)
    visit[start] = True

    while q:
        now_node = q.popleft()
        for next_node, weight in graph[now_node]:
            if not visit[next_node] and weight >= mid:
                visit[next_node] = True
                q.append(next_node)
                if next_node == end:
                    return True
    return False


def binary():
    low,high = min_weight, max_weight
    result = low

    while low<=high:
        mid = (low+high)//2
        if BFS(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result





N,M = map(int,input().split())

graph = [[]for _ in range(N+1)]
min_weight, max_weight = float('inf'),0
for _ in range(M):
    A,B,C = map(int,input().split())
    if min_weight > C:
        min_weight = C
    if max_weight < C:
        max_weight = C
    graph[A].append((B,C))
    graph[B].append((A,C))
start, end = map(int,input().split())

print(binary())



