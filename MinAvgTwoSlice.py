def solution(A):

    for p in range(len(A)):

        if p == 0: 
            avg_1 = (A[0] + A[1]) / 2.0
            avg_2 = (A[0] + A[1] + A[2]) / 3.0

            avg_min = min(avg_1, avg_2)
            start_p = p

        elif p < len(A)-2:
            avg_new_1 = (A[p] + A[p+1]) / 2.0
            avg_new_2 = (A[p] + A[p+1] + A[p+2]) / 3.0

            avg_1 = min(avg_1, avg_new_1)
            avg_2 = min(avg_2, avg_new_2)

            avg_min = (avg_1, avg_2)
        
        elif p > len(A)-2:
            avg


