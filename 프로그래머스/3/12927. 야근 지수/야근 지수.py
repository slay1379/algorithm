import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq



def solution(n,works):
    if sum(works) < n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    while n>0:
        now = -heapq.heappop(works)
        heapq.heappush(works,-(now-1))
        n -= 1

    answer = 0
    for work in works:
        answer += work**2
    return answer