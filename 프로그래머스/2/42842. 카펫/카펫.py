def solution(brown, yellow):
    answer = []
    a = 0
    b = 0
    full = brown + yellow
    
    for i in range(1, full + 1) :
        if full % i == 0 :
            a = i
            b = full // i
            
        if b >= a :
            if (b - 2) * (a - 2) == yellow :
                return [b, a]
            
    return []






