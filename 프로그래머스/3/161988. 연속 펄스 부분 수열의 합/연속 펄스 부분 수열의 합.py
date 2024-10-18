def solution(sequence):
    purse1 = sequence[:]
    purse2 = sequence[:]
    for i in range(len(sequence)):
        if i % 2 == 0:
            purse1[i] *= -1
        if i % 2 != 0:
            purse2[i] *= -1
    
    dp1 = [0]*len(purse1)
    dp2 = [0]*len(purse2)
    dp1[0] = purse1[0]
    dp2[0] = purse2[0]
    
    for i in range(1,len(sequence)):
        if dp1[i-1] < 0:
            dp1[i] = purse1[i]
        if dp1[i-1] >= 0:
            dp1[i] = dp1[i-1]+purse1[i]
        if dp2[i-1] < 0:
            dp2[i] = purse2[i]
        if dp2[i-1] >= 0:
            dp2[i] = dp2[i-1]+purse2[i]
    
    return max(max(dp1),max(dp2))
    