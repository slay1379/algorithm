import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def topology():
    heap = []
    answer = []
    
    for i in range(1,N+1):
        if degree[i] == 0:
            heapq.heappush(heap,i)
    
    while heap:
        now = heapq.heappop(heap)
        answer.append(now)
        
        for next in graph[now]:
            degree[next] -= 1
            if degree[next] == 0:
                heapq.heappush(heap,next)
    
    return answer


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    degree[B] += 1

answer = topology()
print(' '.join(map(str,answer)))