def solution(absolutes, signs):
    answer = 0

    dic = zip(absolutes, signs)
    
    for k, v in dic :
        if v :
            answer += k
        else :
            answer -= k
    
    return answer