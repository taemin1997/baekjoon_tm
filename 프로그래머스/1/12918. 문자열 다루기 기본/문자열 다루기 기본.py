def solution(s):
    answer = False
    l = len(s)
    
    if l == 4 or l == 6 :
        if s.isdigit() :
            answer = True
    
    return answer