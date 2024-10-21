def is_pelindrome(start,end,s):
    left,right = start,end
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def solution(s):
    length = len(s)
    while True:
        limit = len(s)-length+1
        for i in range(limit):
            if is_pelindrome(i,i+length-1,s):
                return length
        length -= 1
        if length <= 0:
            return 0