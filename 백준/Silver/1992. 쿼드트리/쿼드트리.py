import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

def divide(x,y,N):
    global answer
    data = video[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if video[i][j] != data:
                answer += '('
                divide(x,y,N//2)
                divide(x,y+N//2,N//2)
                divide(x+N//2,y,N//2)
                divide(x+N//2,y+N//2,N//2)
                answer += ')'
                return
    answer += data


N = int(input())
video = [list(map(str,input().strip()))for _ in range(N)]
answer = []

divide(0,0,N)
print(''.join(answer))