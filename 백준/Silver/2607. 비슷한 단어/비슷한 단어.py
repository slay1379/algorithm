import sys
input = sys.stdin.readline
from collections import Counter

def is_similar(base,compare):
    base_count = Counter(base)
    compare_count = Counter(compare)

    diff = base_count - compare_count
    diff += compare_count - base_count

    total_diff = sum(diff.values())

    if total_diff == 0:
        return True
    if total_diff == 1:
        return True
    if total_diff == 2 and len(base) == len(compare):
        return True
    return False

N = int(input())
words = [input().strip() for _ in range(N)]
base_word = words[0]

answer = 0
for word in words[1:]:
    if is_similar(base_word,word):
        answer += 1

print(answer)