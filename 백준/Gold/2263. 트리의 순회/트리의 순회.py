import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def find_pre(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    pre_order.append(root)

    root_idx = idx_map[root]

    left_size = root_idx - in_start

    find_pre(in_start,root_idx-1,post_start,post_start+left_size-1)
    find_pre(root_idx+1, in_end,post_start+left_size,post_end-1)


n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
pre_order = []

idx_map = {value: idx for idx, value in enumerate(in_order)}

find_pre(0,n-1,0,n-1)
print(' '.join(map(str,pre_order)))