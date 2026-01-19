import sys
input = sys.stdin.readline

N, M = map(int,input().split())
not_listen = {input().strip() for _ in range(N)}
not_see = {input().strip() for _ in range(M)}

result = sorted(list(not_listen & not_see))

print(len(result))
for name in result:
    print(name)
