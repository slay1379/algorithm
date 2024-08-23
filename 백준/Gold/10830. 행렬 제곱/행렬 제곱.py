import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def square(arr1,arr2):
    newArr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                newArr[i][j] += (arr1[i][k]*arr2[k][j])
            newArr[i][j] %= 1000
    return newArr

def matrix_power(A,B):
    if B == 1:
        return [[A[i][j] % 1000 for j in range(N)] for i in range(N)]

    half_power = matrix_power(A,B//2)
    half_squared = square(half_power, half_power)

    if B%2 == 1:
        return square(half_squared,A)
    else:
        return half_squared


N,B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

result = matrix_power(A,B)

for row in result:
    print(' '.join(map(str,row)))
