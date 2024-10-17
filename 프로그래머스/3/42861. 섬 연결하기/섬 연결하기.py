import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq

def find_root(parent,a):
    if parent[a] != a:
        parent[a] = find_root(parent,parent[a])
    return parent[a]

def union(a,b,parent):
    root_a = find_root(parent,a)
    root_b = find_root(parent,b)
    if root_a == root_b:
        return False
    parent[root_b] = root_a
    return True


def solution(n, costs):
    answer = 0
    parent = [i for i in range(100)]
    costs = sorted(costs,key=lambda x:x[2])
    for start,end,cost in costs:
        if union(start,end,parent):
            answer += cost

    return answer

