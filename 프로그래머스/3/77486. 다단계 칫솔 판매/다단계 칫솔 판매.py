def distribution(now,parents,index,result,amount):
    if now == "-" or amount<1:
        return
    if amount // 10 <= 0:
        result[index[now]] += amount
    if amount // 10 > 0:
        result[index[now]] += amount - (amount//10)
    distribution(parents[now],parents,index,result,amount//10)

def solution(enroll, referral, seller, amount):
    result = [0]*len(enroll)
    parents = {}
    index = {}
    for i in range(len(enroll)):
        parents[enroll[i]] = referral[i]
        index[enroll[i]] = i
    
    for i in range(len(seller)):
        now = seller[i]
        distribution(now,parents,index,result,amount[i]*100)
    
    return result
        
    