import sys
N, K = map(int,sys.stdin.readline().split())
yose = []
circle = [i for i in range(1,N+1)]
now = -1
while True:
    if not (circle):
        break
    now += K
    now = now % N
    yose.append(circle[now])
    del circle[now]
    now -= 1
    N -= 1
output = ', '.join(map(str,yose))
output = '<' + output + '>'
print(output)