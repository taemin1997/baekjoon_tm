def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2) :
        binary = bin(a | b)[2:].zfill(n)
        binary = binary.replace('1', '#').replace('0', ' ')
        answer.append(binary)
    
    return answer