def solution(A):
    front = A[0]
    end = sum(A[1:])
    dis = abs(front - end)
    
    for p in range(1, len(A)-1):
        front += A[p]
        end -= A[p]
        
        dis_new = abs(front - end)
        
        if dis_new <= dis:
            dis = dis_new
        else:
            pass
        
    return dis