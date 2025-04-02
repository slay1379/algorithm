import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
answer = 0
for _ in range(N):
    word = list(input().strip())
    stack = []
    for element in word:
        if stack:
            if stack[-1] == element:
                stack.pop()
            else:
                stack.append(element)
        else:
            stack.append(element)
    if not stack:
        answer += 1

print(answer)