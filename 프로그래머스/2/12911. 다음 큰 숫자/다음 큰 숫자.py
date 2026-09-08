def solution(n):
    answer = 0
    count = 0
    temp = n
    b_n = bin(n)[2:]
    
    for b in b_n :
        if b == '1' :
            count += 1
    
    while True :
        temp += 1
        
        b_temp = bin(temp)[2:]
        t_count = 0
        
        for t in b_temp :
            if t == '1' :
                t_count += 1
        
        
        
        if t_count == count :
            answer = temp
            break
        
    
    return answer