import sys
N = int(sys.stdin.readline())
answer = ''

if N == 0:
    print('0')
    quit()

while N != 1:
    if N % -2 == -1:
        N=N-1
        answer = str(N%-2+1) + answer
    else:
        answer = str(N%-2) + answer
    N = N // -2
answer = str(1) + answer

print(answer)