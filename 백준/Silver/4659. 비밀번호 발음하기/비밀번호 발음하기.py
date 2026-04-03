import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

while True:
    password = input().strip()

    if password == 'end':
        break
    flag = False
    accept = True
    prev = ''
    mo,ja = 0,0
    for ch in password:
        if prev == ch:
            if ch != 'e' and ch != 'o':
                accept = False
                break
        if ch in ['a','e','i','o','u']:
            ja = 0
            mo += 1
            flag = True
        else:
            mo = 0
            ja += 1
        if ja >= 3 or mo >= 3:
            accept = False
            break
        prev = ch

    if flag and accept:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")