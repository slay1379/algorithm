import sys
input = sys.stdin.readline
from collections import deque
import heapq

N,C = map(int,input().split())
message = list(map(int,input().split()))

freq = {}
first_index = {}

for i, num in enumerate(message):
    if num not in freq:
        freq[num] = 0
        first_index[num] = i
    freq[num] += 1

unique_nums = list(freq.keys())
unique_nums.sort(key=lambda  x: (-freq[x],first_index[x]))

result = []
for num in unique_nums:
    result.extend([num] * freq[num])

print(*result)
