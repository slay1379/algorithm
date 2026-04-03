import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N, C = map(int,input().split())
seq = list(map(int,input().split()))

count = Counter(seq)

order = {}
for i,num in enumerate(seq):
    if num not in order:
        order[num] = i

seq.sort(key=lambda x: (-count[x],order[x]))
print(*seq)

