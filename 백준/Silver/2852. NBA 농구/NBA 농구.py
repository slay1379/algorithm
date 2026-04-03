import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N = int(input())
first_stack,second_stack = 0,0
first_time,second_time = 0,0
prev = 0
score = [0,0,0]

for _ in range(N):
    line = input().strip()
    team, time = line.split(' ')
    hour = int(time[:2])
    minute = int(time[3:5])

    score[int(team)] += 1

    if prev == 0:
        if score[1] > score[2]:
            first_stack = hour*60 + minute
            prev = 1
        elif score[2] > score[1]:
            second_stack = hour*60 + minute
            prev = 2

    if score[1] == score[2]:
        if prev == 1:
            first_time += (hour*60+minute)-first_stack
            prev = 0
        elif prev == 2:
            second_time += (hour*60+minute)-second_stack
            prev = 0

if score[1] > score[2]:
    first_time += 48*60 - first_stack
elif score[2] > score[1]:
    second_time += 48*60 - second_stack

first_hour = first_time//60
first_minute = first_time%60
second_hour = second_time//60
second_minute = second_time%60

print(f'{first_hour:02d}:{first_minute:02d}')
print(f'{second_hour:02d}:{second_minute:02d}')