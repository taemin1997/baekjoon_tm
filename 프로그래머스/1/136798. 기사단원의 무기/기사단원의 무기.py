def solution(number, limit, power):
    answer = 0
    g_li = []
    
    for n in range(1, number + 1) :
        g = countG(n)
    
        if g > limit :
            g = power
    
        g_li.append(g)
        
    answer = sum(g_li)
    
    return answer


def countG(number) :
    count = 0
    
    for n in range(1, int(number ** 0.5) + 1):
        if number % n == 0:
            count += 2
            
            if n * n == number:
                count -= 1
            
    return count