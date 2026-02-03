import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
weights = {}

for word in words:
    for i in range(len(word)):
        if word[i] not in weights:
            weights[word[i]] = 10**(len(word)-i-1)
        else:
            weights[word[i]] += 10**(len(word)-i-1)

sorted_weights = sorted(weights.values(), reverse=True)

result = 0
now = 9

for weight in sorted_weights:
    result += now*weight
    now -= 1

print(result)
