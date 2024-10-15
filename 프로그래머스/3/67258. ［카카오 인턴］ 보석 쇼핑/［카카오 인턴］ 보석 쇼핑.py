import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from itertools import permutations
from collections import deque
from collections import defaultdict
import heapq



def solution(gems):
    gems = ['']+gems
    gems_count = {}
    all_gems = set()
    start = 1
    dp = [-1]*(len(gems))

    for i in range(1,len(gems)):
        all_gems.add(gems[i])
    all_gems_type = len(all_gems)

    for i in range(1,len(gems)):
        gems_count[gems[i]] = gems_count.get(gems[i],0)+1
        if len(gems_count) >= all_gems_type:
            while gems_count[gems[start]] >= 2:
                gems_count[gems[start]] -= 1
                if gems_count[gems[start]] == 0:
                    del gems_count[gems[start]]
                start += 1
            dp[i] = start

    answer = [0,len(gems)]
    for i in range(1,len(dp)):
        if dp[i] == -1:
            continue
        if i-dp[i] < answer[1]-answer[0]:
            answer = [dp[i],i]
    return answer


