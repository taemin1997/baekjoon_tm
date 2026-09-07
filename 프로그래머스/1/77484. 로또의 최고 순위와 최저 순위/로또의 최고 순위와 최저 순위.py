def solution(lottos, win_nums):
    answer = []
    li = []
    count = 0
    z_c = 0
    
    for l in lottos :
        if l == 0 :
            z_c += 1
        for w in win_nums :
            if l == w :
                count += 1
                
    ma = 7 - (count + z_c)
    mi = 7 - count
    
    if ma > 6 :
        ma = 6
        
    if mi > 6 :
        mi = 6
    
    answer = [ma, mi]
    
    
    return answer







