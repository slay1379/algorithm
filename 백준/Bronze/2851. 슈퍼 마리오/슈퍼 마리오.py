import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

mushroom = []
for _ in range(10):
    mushroom.append(int(input()))
total = 0
for i in range(len(mushroom)):
    if total + mushroom[i] > 100:
        if 100-total < total+mushroom[i] - 100:
            print(total)
        else:
            print(total+mushroom[i])
        break
    else:
        total += mushroom[i]
else:
    print(total)

