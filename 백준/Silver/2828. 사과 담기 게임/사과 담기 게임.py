import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N,M = map(int,input().split())
J = int(input())
answer = 0
head, tail = 1,M

for _ in range(J):
    apple = int(input())
    if apple < head:
        dis = head - apple
        answer += dis
        head -= dis
        tail -= dis
    elif apple > tail:
        dis = apple - tail
        answer += dis
        head += dis
        tail += dis

print(answer)