import heapq

def solution(operation):
    min_heap = []
    max_heap = []
    in_heap_number = {}
    for oper in operation:
        o = oper[:1]
        n = int(oper[1:])
        if o == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            in_heap_number[n] = in_heap_number.get(n,0) + 1
        if o == 'D':
            if n == 1:
                while max_heap:
                    now = -heapq.heappop(max_heap)
                    if in_heap_number[now] > 0:
                        in_heap_number[now] -= 1
                        break
            if n == -1:
                while min_heap:
                    now = heapq.heappop(min_heap)
                    if in_heap_number[now] > 0:
                        in_heap_number[now] -= 1
                        break

    valid_number = [key for key, count in in_heap_number.items() if count > 0]
    
    if valid_number:
        return [max(valid_number),min(valid_number)]
    else:
        return [0,0]