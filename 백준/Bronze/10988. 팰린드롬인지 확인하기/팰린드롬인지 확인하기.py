import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations

word = input().strip()
l = len(word)

if l % 2 == 0:
    idx = l // 2
else:
    idx = l//2+1

answer = 1
for i in range(idx,l):
    if word[i] != word[l-1-i]:
        answer = 0
        break

print(answer)