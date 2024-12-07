def solution(scores):
    wanho = scores[0]
    sum_wanho = sum(wanho)
    
    scores.sort(key=lambda x : (-x[0],x[1]))
    
    new = []
    max_peer = 0
    
    for work,peer in scores:
        if peer < max_peer:
            if [work,peer] == wanho:
                return -1
        else:
            if peer > max_peer:
                max_peer = peer
            new.append(work+peer)
    new.sort(reverse=True)
    for i in range(len(new)):
        if new[i] == sum_wanho:
            return i+1
        
    