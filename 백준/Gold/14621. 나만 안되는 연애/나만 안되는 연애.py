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

def cal_min_dis():
    answer = 0
    edge_count = 0
    for dis,a,b in edges:
        if sex[a] != sex[b]:
            if union(a,b):
                answer += dis
                edge_count += 1
                if edge_count == N-1:
                    return answer
    return -1


N,M = map(int,input().split())
sex = ['0'] + list(map(str,input().strip().split()))

edges = []
parent = [i for i in range(N+1)]

for _ in range(M):
    u,v,d = map(int,input().split())
    edges.append((d,u,v))

edges.sort()

print(cal_min_dis())