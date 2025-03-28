import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
pattern = input().strip()
files = [input().strip() for _ in range(N)]

idx = pattern.index('*')
head = pattern[:idx]
tail = pattern[idx+1:]

for file in files:
    if len(file) < len(head) + len(tail):
        print("NE")
        continue
    if file.startswith(head) and file.endswith(tail):
        print("DA")
    else:
        print("NE")