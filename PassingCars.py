def solution(A):
    count_1 = sum(A)
    pair_count = 0
    last_0 = -1
    
    if count_1 > 1000000000:
        return -1
    else:
        for i in range(len(A)):
            if A[i] == 0:
                pair_count += count_1 - (i - last_0 - 1)
                count_1 -= (i - last_0 - 1)
                last_0 = i
                
                if pair_count > 1000000000:
                    pair_count = -1
                    break
            
    return pair_count