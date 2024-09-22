import sys
input = sys.stdin.readline

code = list(input().strip())
N = int(input())
words = [input().strip() for _ in range(N)]
for _ in range(1,27):
    code = [chr((ord(c)-ord('a')+1)%26+ord('a'))for c in code]
    if any(word in ''.join(code) for word in words):
        print(''.join(code))
        break