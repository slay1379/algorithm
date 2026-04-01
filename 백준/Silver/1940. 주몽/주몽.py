import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N = int(input())
M = int(input())
ingredient = list(map(int,input().split()))

ingredient.sort()
left,right = 0,N-1

answer = 0
while left<right:
    plus = ingredient[left] + ingredient[right]
    if plus == M:
        answer += 1
        right -= 1
        left += 1
    elif plus > M:
        right -= 1
    else:
        left += 1

print(answer)