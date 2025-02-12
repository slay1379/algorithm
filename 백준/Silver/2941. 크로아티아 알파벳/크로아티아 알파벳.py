import sys
input = sys.stdin.readline
from collections import deque
import heapq

word = input().strip()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
gap = 0

for w in croatia:
    gap += word.count(w)

print(len(word)-gap)

