import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())


max_answer = -sys.maxsize
min_answer = sys.maxsize

def cal(i, result, add, sub, mul ,div):
    global max_answer, min_answer
    if i == N:
        max_answer = max(result,max_answer)
        min_answer = min(result,min_answer)
        return
    else:
        if add:
            cal(i+1,result+A[i],add-1,sub,mul,div)
        if sub:
            cal(i+1,result-A[i],add,sub-1,mul,div)
        if mul:
            cal(i+1,result*A[i],add,sub,mul-1,div)
        if div:
            if result<0:
                cal(i+1,-(-result//A[i]),add,sub,mul,div-1)
            else:
                cal(i+1,result//A[i],add,sub,mul,div-1)

cal(1,A[0],add,sub,mul,div)

print(max_answer)
print(min_answer)