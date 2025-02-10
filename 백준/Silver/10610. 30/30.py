import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
nums = []
while N>0:
    nums.append(N%10)
    N //= 10

if 0 not in nums or sum(nums)%3 != 0:
    print(-1)
else:
    answer = 0
    nums.sort(reverse = True)
    for i in range(len(nums)):
        answer += nums[i]
        answer *= 10
    print(answer//10)