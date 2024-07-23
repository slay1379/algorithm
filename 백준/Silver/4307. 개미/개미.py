import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def solve(ants):
    min_time, max_time = 0,0
    for ant in ants:
        fast_time = min(ant,l-ant)
        slow_time = max(ant,l-ant)

        if fast_time > min_time:
            min_time = fast_time
        if slow_time > max_time:
            max_time = slow_time

    return min_time,max_time


T = int(input())
for _ in range(T):
    l,n = map(int,input().split())
    ants = []
    for _ in range(n):
        ants.append(int(input()))
    min_time,max_time = solve(ants)
    print(min_time,max_time)

