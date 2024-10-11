import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


def solution(n,stations,w):
    answer = 0
    coverage = 2*w+1

    current_position = 1

    for station in stations:
        start = max(1, station - w)
        end = min(n, station + w)

        if current_position < start:
            gap = start - current_position
            station_count = gap // coverage
            if gap % coverage > 0:
                station_count += 1
            answer += station_count

        current_position = end + 1

    if current_position <= n:
        gap = n - current_position + 1
        station_count = gap // coverage
        if gap % coverage > 0:
            station_count += 1
        answer += station_count

    return answer
