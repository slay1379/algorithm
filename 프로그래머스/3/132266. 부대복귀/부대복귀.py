import sys
import re

input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for area1, area2 in roads:
        graph[area1].append(area2)
        graph[area2].append(area1)
        
    distance = [-1]*(n+1)
    distance[destination] = 0
    q = deque()
    q.append(destination)
    
    while q:
        now = q.popleft()
        for node in graph[now]:
            if distance[node] == -1 or distance[node] > distance[now] + 1:
                distance[node] = distance[now] + 1
                q.append(node)
    
    answer = []
    for source in sources:
        answer.append(distance[source])
    
    return answer
    
    
    
            
                
    
    