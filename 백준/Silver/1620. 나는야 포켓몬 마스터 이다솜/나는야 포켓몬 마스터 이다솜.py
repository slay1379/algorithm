import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations

N,M = map(int,input().split())
pocketmons_name = dict()
pocketmons_num = dict()

for i in range(1,N+1):
    pocketmon = input().strip()
    pocketmons_name[pocketmon] = i
    pocketmons_num[i] = pocketmon

for _ in range(M):
    line = input().strip()
    if line.isdigit():
        print(pocketmons_num[int(line)])
    else:
        print(pocketmons_name[line])
