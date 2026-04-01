import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

line = input().strip()
result = [[char, line.count(char)] for char in set(line)]

flag = False
mid = ''
for i in range(len(result)):
    if result[i][1] % 2 != 0:
        if flag:
            print("I'm Sorry Hansoo")
            exit()
        flag = True
        mid = result[i][0]

result.sort()

front = ''
for ch, num in result:
    front += ch*(num//2)

back = front[::-1]
print(front+mid+back)