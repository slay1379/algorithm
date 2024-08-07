import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])
    return parent[a]

def union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        parent[b_root] = a_root
        return True
    return False

def cal_min_cost():
    answer = 0
    edge_count = 0
    for cost,i,j in edges:
        if union(i,j):
            answer += cost
            edge_count += 1
            if edge_count == N-1:
                return answer

N = int(input())
if N == 1:
    print(0)
    exit()
costs = [list(map(int,input().split())) for _ in range(N)]

edges = []
parent = [i for i in range(N)]

for i in range(N):
    for j in range(i+1,N):
        edges.append((costs[i][j],i,j))

edges.sort()


print(cal_min_cost())