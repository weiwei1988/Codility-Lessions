def solution(N, A):
    counter = [0 for i in range(N)]
    max_value = 0
    last_update = 0
    
    for i in range(len(A)):
        if A[i] <= N:
            if counter[A[i] - 1] < last_update:
                counter[A[i] - 1] = last_update
            
            counter[A[i] - 1] += 1
            max_value = max(max_value, counter[A[i] - 1])
        
        elif A[i] == N + 1:
            last_update = max_value
            
        else:
            pass
    
    for i in range(len(counter)):
        if counter[i] < last_update:
            counter[i] = last_update
    
    return counter