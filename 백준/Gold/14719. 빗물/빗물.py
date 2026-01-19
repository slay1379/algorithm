import sys
input = sys.stdin.readline

H,W = map(int,input().split())
blocks = list(map(int,input().split()))

rainwater = 0

for i in range(1,W-1):
    left,right = i,i
    max_left, max_right = i,i
    while True:
        left -= 1
        if blocks[left] > blocks[max_left]:
            max_left = left
        if left == 0:
            break
    while True:
        right += 1
        if blocks[right] > blocks[max_right]:
            max_right = right
        if right == W-1:
            break
    if max_left == i or max_right == i:
        continue
    rainwater += min(blocks[max_left], blocks[max_right]) - blocks[i]

print(rainwater)
