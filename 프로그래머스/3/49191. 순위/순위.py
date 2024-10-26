import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq


def solution(n, results):
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)
    
    for winner, loser in results:
        win_graph[winner].add(loser)
        lose_graph[loser].add(winner)
    
    for i in range(1,n+1):
        q = deque(win_graph[i])
        while q:
            now = q.popleft()
            for next in win_graph[now]:
                if next not in win_graph[i]:
                    win_graph[i].add(next)
                    q.append(next)
    
        q = deque(lose_graph[i])
        while q:
            now = q.popleft()
            for next in lose_graph[now]:
                if next not in lose_graph[i]:
                    lose_graph[i].add(next)
                    q.append(next)
    
    answer = 0
    for i in range(1,n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1
    
    return answer
    
    
    
    
        

    
    