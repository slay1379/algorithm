import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq

line = input()
nums = []
opers = []
now_num = ''

for i in range(len(line)):
    if line[i] != '+' and line[i] != '-':
        now_num += line[i]
    else:
        nums.append(int(now_num))
        now_num = ''
        opers.append(line[i])
nums.append(int(now_num.strip()))

i = 0
while True:
    if len(opers) <= i:
        break
    if opers[i] == '+':
        nums[i] += nums[i+1]
        del(nums[i+1])
        del(opers[i])
        continue
    i += 1

answer = nums[0]
for i in range(1,len(nums)):
    answer -= nums[i]

print(answer)