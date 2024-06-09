import sys
input = sys.stdin.readline
from collections import Counter
from collections import defaultdict

N,M = map(int,input().split())
seq = list(map(int,input().split()))
count = defaultdict(int)
sum = [0]*(N+1)
for i in range(1,N+1):
    sum[i] = (sum[i-1]+seq[i-1])%M
    count[sum[i]] += 1

count[0] += 1

answer = 0
for v in count.values():
    answer += v * (v-1)//2

print(answer)