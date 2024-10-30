import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for n1,n2,cost in fares:
        graph[n1].append((n2,cost))
        graph[n2].append((n1,cost))
    
    from_s = [-1]*(n+1)
    to_a = [-1]*(n+1)
    to_b = [-1]*(n+1)
    
    from_s[s] = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        for node,cost in graph[now]:
            if from_s[node] == -1 or from_s[now] + cost < from_s[node]:
                from_s[node] = from_s[now] + cost
                q.append(node)
    
    to_a[a] = 0
    q = deque()
    q.append(a)
    while q:
        now = q.popleft()
        for node,cost in graph[now]:
            if to_a[node] == -1 or to_a[now] + cost < to_a[node]:
                to_a[node] = to_a[now] + cost
                q.append(node)
                
    to_b[b] = 0
    q = deque()
    q.append(b)
    while q:
        now = q.popleft()
        for node,cost in graph[now]:
            if to_b[node] == -1 or to_b[now] + cost < to_b[node]:
                to_b[node] = to_b[now] + cost
                q.append(node)
    
    answer = from_s[1]+to_a[1]+to_b[1]
    for i in range(2,n+1):
        if answer < 0:
            answer = from_s[i]+to_a[i]+to_b[i]
        if from_s[i] != -1 and to_a[i] != -1 and to_b[i] != -1:
            if answer > from_s[i]+to_a[i]+to_b[i]:
                answer = from_s[i]+to_a[i]+to_b[i]
                
    return answer
    
    
    
    