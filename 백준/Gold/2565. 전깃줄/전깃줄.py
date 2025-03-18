import sys
import heapq
input = sys.stdin.readline
import bisect

N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]

lines.sort()
B_values = [b for _, b in lines]
LIS = []

for b in B_values:
    pos = bisect.bisect_left(LIS, b)
    if pos == len(LIS):
        LIS.append(b)
    else:
        LIS[pos] = b

print(N-len(LIS))