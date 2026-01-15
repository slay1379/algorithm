import sys
input = sys.stdin.readline

H,W = map(int,input().split())
blocks = list(map(int,input().split()))

rainwater = 0

for i in range(len(blocks)):
    for height in range(blocks[i],0,-1):
        cnt = 0
        for j in range(i + 1, len(blocks)):
            if j >= len(blocks):
                break
            if blocks[j] >= height:
                rainwater += cnt
                break
            cnt += 1


print(rainwater)
