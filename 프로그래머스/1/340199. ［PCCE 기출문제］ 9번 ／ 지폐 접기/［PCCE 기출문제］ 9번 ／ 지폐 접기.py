def solution(wallet, bill):
    answer = 0
    bill.sort()
    wallet.sort()
    n = bill[0]
    m = bill[1]
    w = wallet[0]
    h = wallet[1]
    
    while n > w or m > h :
        if n > m :
            n = n // 2
        else : 
            m = m // 2
            
        n, m = sorted([n, m])
        answer += 1
           
    return answer



