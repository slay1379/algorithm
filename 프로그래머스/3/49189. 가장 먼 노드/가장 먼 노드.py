import sys
import re

input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    q = deque()
    q.append(1)
    distances = [-1]*(n+1)
    distances[1] = 0
    while q:
        now = q.popleft()
        for node in graph[now]:
            if distances[node] == -1 or distances[node] > distances[now]+1:
                distances[node] = distances[now] + 1
                q.append(node)
    
    max_distance = max(distances)
    answer = 0
    for distance in distances:
        if distance == max_distance:
            answer += 1
    
    return answer
        