import sys
input = sys.stdin.readline

N,S = map(int,input().split())
seq = list(map(int,input().split()))

answer = 0
left,right = 0,0
current_sum = seq[0]

while True:
    if left == right:
        if seq[left] >= S:
            answer = 1
            break
        if right == N-1:
            break
        right += 1
        current_sum += seq[right]
        continue
    if current_sum >= S or right == N-1:
        if current_sum >= S and (answer == 0 or answer > right-left+1):
            answer = right-left+1
        current_sum -= seq[left]
        left += 1
    else:
        right += 1
        current_sum += seq[right]

print(answer)