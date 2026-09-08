def solution(s):
    li = []
    
    for c in s :
        if c == '(' :
            li.append(c)
        else :
            if not li :
               return False
            li.pop()

    return len(li) == 0