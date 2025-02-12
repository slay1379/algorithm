import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())

nums = []
for i in range(1,10):
    for j in range(-9,10):
        if 0<= i + j*2 <= 9:
            num = (i*100) + ((i+j)*10) + (i+j*2)
            nums.append(num)

if N<=99:
    print(N)
else:
    gap = 0
    for i in range(len(nums)):
        gap = i
        if nums[i] > N:
            break
        gap += 1
    print(99+gap)