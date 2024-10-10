import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


def solution(routes):
    routes.sort(key=lambda x:x[1])
    cameras = 0
    last_camera = -30001

    for route in routes:
        entry, exit = route

        if entry > last_camera:
            cameras += 1
            last_camera = exit
    
    return cameras

