import sys
import re

input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq

def solution(n, t, m, timetable):
    timetable.sort()
    crew_timetable = deque(timetable)
    bus_timetable = ["09:00"]
    first_bus = 9*60
    for i in range(n-1):
        first_bus += t
        time, minute = first_bus//60, first_bus%60
        bus_time = str(time).zfill(2) + ":" + str(minute).zfill(2)
        bus_timetable.append(bus_time)
    
    print(crew_timetable)
    print(bus_timetable)
    for time in bus_timetable:
        now_people = 0
        bus = []
        while crew_timetable and crew_timetable[0] <= time and now_people < m:
            bus.append(crew_timetable.popleft())
            now_people += 1
        if n == 1:
            print(bus)
            if len(bus) < m:
                return time
            time,minute = bus[-1].split(':')
            answer_time = (int(time)*60+int(minute)-1) // 60
            answer_minute = (int(time)*60+int(minute)-1) % 60
            return str(answer_time).zfill(2) + ":" + str(answer_minute).zfill(2)
        n -= 1
        
    
        
    